from query_debugger import query_debugger
from django.views       import View
from django.http        import JsonResponse
from django.db.models   import Q, Count

from jobpostings.models import Company, JobPosting, Tag

class SearchView(View):
    @query_debugger
    def get(self, request):
        region   = request.GET.get("region")
        query    = request.GET.get("query")
        order_by = request.GET.get("orderBy", "latest")
        tags     = request.GET.getlist("tag")
        offset   = int(request.GET.get("offset", 0))
        limit    = int(request.GET.get("limit", 20))
        sorted_dict = {
            "latest" : "-created_at",
            "popular" : "bookmark_count",
            "apply" : "apply_count"
        }

        q = Q()

        if region:
            q &= Q(company__region__name = region)
        if query:
            q &= Q(company__name__contains = query) | Q(title__contains= query)
        if tags:
            q &= Q(tags__name__in=tags)

        job_postings = JobPosting.objects.select_related("job", "experience", "company", "company__region", "company__region__country").annotate(bookmark_count=Count("bookmark"), apply_count=Count("apply")).filter(q).distinct().order_by(sorted_dict[order_by])[offset : offset + limit]
        job_posting_list = [{
                "id" : job_posting.id,
                "title" : job_posting.title,
                "salary" : job_posting.salary,
                "experience" : job_posting.experience.name,
                "imageUrl" : job_posting.image_url,
                "bookmarkCount" : job_posting.bookmark_count,
                "apply_Count" : job_posting.apply_count,
                "company" : {
                    "id" : job_posting.company.id,
                    "name" : job_posting.company.name,
                    "region" : job_posting.company.region.name,
                    "country" : job_posting.company.region.country.name,
                },
                "job" : {
                    "id" : job_posting.job.id,
                    "name" :job_posting.job.name,
                },
        } for job_posting in job_postings]

        return JsonResponse({"message":"SUCCESS", "result":job_posting_list}, status=200)

# ? : 제대로 가져오고 있는건가?
class SuggestView(View):
    @query_debugger
    def get(self, request):
        query    = request.GET.get("query")
        offset   = int(request.GET.get("offset", 0))
        limit    = int(request.GET.get("limit", 4))
        q        = Q()
        t        = Q()

        if query:
            q &= Q(title__contains= query)
            t &= Q(name__contains=query)
        else:
            return JsonResponse({"message":"QUERY_REQUIRED"}, status=400)

        job_postings = JobPosting.objects.filter(q).values("id", "title")[offset : offset + limit]
        tags         = Tag.objects.filter(t).values("id", "name")[offset : offset + limit]
        companies    = Company.objects.filter(t).values("id", "name")[offset : offset + limit]
        result       = {
            "jobPostings" : [{
                "id" : job_posting["id"],
                "title" : job_posting["title"],
            # ! : values를 쓰면 annotate의 결과도 dict의 key value로써 들어가게 된다.
            }for job_posting in job_postings],
            "tags" : [{
                "id" : tag["id"],
                "name" : tag["name"],
            }for tag in tags],
            "companies" : [{
                "id" : company["id"],
                "name" : company["name"],
            }for company in companies],
        }

        return JsonResponse({"message":"SUCCESS", "result":result}, status=200)
import json
from json.decoder       import JSONDecodeError
from django.views       import View
from django.http        import JsonResponse
from django.db.models   import Q, Count, Avg

from jobpostings.models import TagCategory, JobGroup, Company, JobPosting, Tag, Job
from resumes.models     import Apply, Resume
from users.models       import Bookmark
from utils              import lose_authorization, authorization

class TagCategoryView(View):
    def get(self, request):
        tag_categories    = TagCategory.objects.prefetch_related("tag").all()

        tag_category_list = [{
                "id"                 : tag_category.id,
                "name"               : tag_category.name,
                "is_multiple_choice" : tag_category.is_multiple_choice,
                "tags"               : [{
                    "id"   : tag.id,
                    "name" : tag.name,
                } for tag in tag_category.tag.all()],
            } for tag_category in tag_categories]

        return JsonResponse({"message" : "SUCCESS", "result" : tag_category_list}, status=200)

class JobGroupView(View):
    def get(self, request):
        job_groups     = JobGroup.objects.prefetch_related("job").all()

        job_group_list = [{
                "id"   : job_group.id,
                "name" : job_group.name,
                "jobs" : [{
                    "id"   : job.id,
                    "name" : job.name,
                } for job in job_group.job.all()],
            } for job_group in job_groups]

        return JsonResponse({"message" : "SUCCESS", "result" : job_group_list}, status=200)

class PostingsView(View):
    def get(self, request):
        region      = request.GET.get("region")
        query       = request.GET.get("query")
        job         = request.GET.get("job")
        experience  = request.GET.get("experience")
        order_by    = request.GET.get("orderBy", "latest")
        tags        = request.GET.getlist("tag")
        offset      = int(request.GET.get("offset", 0))
        limit       = int(request.GET.get("limit", 20))
        sorted_dict = {
            "latest" : "-created_at",
            "popular" : "bookmark_count",
            "apply" : "apply_count"
        }

        q = Q()

        if region:
            q &= Q(company__region__name=region)
        if query:
            q &= Q(company__name__contains=query) | Q(title__contains=query)
        if job:
            q &= Q(job__name=job)
        if experience:
            q &= Q(experience__name=experience)
        if tags:
            q &= Q(tags__name__in=tags)
        
        queryset     = JobPosting.objects.select_related("job", "experience", "company", "company__region", "company__region__country").annotate(bookmark_count=Count("bookmark"), apply_count=Count("apply")).filter(q).distinct().order_by(sorted_dict[order_by])
        job_postings = queryset[offset * limit : (offset * limit) + limit] 
        job_posting_count = queryset.aggregate(Count("id"))["id__count"]
        
        job_posting_list = [{
            "id"            : job_posting.id,
            "title"         : job_posting.title,
            "salary"        : job_posting.salary,
            "experience"    : job_posting.experience.name,
            "imageUrl"      : job_posting.image_url,
            "bookmarkCount" : job_posting.bookmark_count,
            "apply_Count"   : job_posting.apply_count,
            "company"       : {
                "id"      : job_posting.company.id,
                "name"    : job_posting.company.name,
                "region"  : job_posting.company.region.name,
                "country" : job_posting.company.region.country.name,
            },
            "job"           : {
                "id"   : job_posting.job.id,
                "name" : job_posting.job.name,
            }
        } for job_posting in job_postings]

        return JsonResponse({"message":"SUCCESS", "count" : job_posting_count, "result":job_posting_list}, status=200)

class SuggestView(View):
    def get(self, request):
        try:
            query        = request.GET["query"]
            job_postings = JobPosting.objects.filter(title__contains= query).values("id", "title")[0:4]
            tags         = Tag.objects.filter(name__contains=query).values("id", "name")[0:4]
            companies    = Company.objects.filter(name__contains=query).values("id", "name")[0:4]
            result       = {
                "jobPostings" : [{
                    "id"    : job_posting["id"],
                    "title" : job_posting["title"],
                }for job_posting in job_postings],
                "tags" : [{
                    "id"   : tag["id"],
                    "name" : tag["name"],
                }for tag in tags],
                "companies" : [{
                    "id"   : company["id"],
                    "name" : company["name"],
                }for company in companies],
            }

            return JsonResponse({"message":"SUCCESS", "result":result}, status=200)

        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)

class PostingView(View):
    @lose_authorization
    def get(self, request, posting_id):
        user = request.user

        if not JobPosting.objects.filter(id=posting_id).exists():
            return JsonResponse({"message" : "404 NOT_FOUND"}, status=401)

        job_posting = JobPosting.objects.get(id=posting_id)
        bookmark    = Bookmark.objects.filter(user=user, job_posting=posting_id).exists()

        job_posting_info = {
            "job_posting_id"    : job_posting.pk,
            "job_posting_title" : job_posting.title,
            "salary"            : job_posting.salary,
            "due_date"          : job_posting.due_date,
            "image_url"         : job_posting.image_url,
            "job"               : job_posting.job.name,
            "experience"        : job_posting.experience.name,
            "bookmark"          : bookmark,
            "company_info"      : {
                "company_name" : job_posting.company.name,
                "coordinate"   : job_posting.company.coordinate,
            },
            "description"       : {
                "benefit"          : job_posting.benefit,
                "intro"            : job_posting.description,
                "main_task"        : job_posting.main_task,
                "preference_point" : job_posting.preference,
                "requirements"     : job_posting.requirement
            },
            "tag_info"          : [ tag.name for tag in job_posting.tags.all()]
        }

        return JsonResponse({"message":"SUCCESS", "result":job_posting_info}, status=200)

class ApplyView(View):
    @authorization
    def post(self, request, posting_id):
        try:
            data    = json.loads(request.body)
            resumes = Resume.objects.filter(id__in=data["resumeList"], user=request.user)

            if not resumes.exists():
                return JsonResponse({"message" : "NO_RESUME_SELECTED"}, status=400)
            
            if Apply.objects.filter(job_posting__id=posting_id, user=request.user).exists():
                return JsonResponse({"message" : "APPLY_ALREADY_EXIST"}, status=400)

            Apply.objects.create(user=request.user, job_posting_id=posting_id).resume.set(resumes)
            
            return JsonResponse({"message":"SUCCESS"}, status=200)
        
        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)

        except JSONDecodeError:
            return JsonResponse({"message" : "JDON_DECODE_ERROR"}, status=400)
            
class SalaryView(View):
    def get(self, request):
        job_group = request.GET.get("jobGroup")
        job       = request.GET.get("job")

        if not job or not job_group:
            return JsonResponse({"message":"QUERY_REQUIRED"}, status=400)

        model    = JobGroup if job == "전체" else Job
        name     = job_group if job == "전체" else job
        key      = "job__job_posting" if job == "전체" else "job_posting"
        related  = ("job", "job__job_posting", "job__job_posting__experience") if job == "전체" else ("job_posting", "job_posting__experience")
        
        if not model.objects.filter(name=name).exists():
            return JsonResponse({"message":"DATA_NOT_FOUND"}, status=404)
        
        job_or_group = model.objects.filter(name=name).prefetch_related(*related)\
            .annotate(
                avg_total       = Avg(f"{key}__salary"),
                posting_count   = Count(key),
                avg_zero        = Avg(f"{key}__salary", filter=Q(**{f"{key}__experience__name":"신입"} )),
                avg_one         = Avg(f"{key}__salary", filter=Q(**{f"{key}__experience__name":"1년차"} )),
                avg_two         = Avg(f"{key}__salary", filter=Q(**{f"{key}__experience__name":"2년차"} )),
                avg_three       = Avg(f"{key}__salary", filter=Q(**{f"{key}__experience__name":"3년차"} )),            
                avg_four        = Avg(f"{key}__salary", filter=Q(**{f"{key}__experience__name":"4년차"} )),
                avg_five        = Avg(f"{key}__salary", filter=Q(**{f"{key}__experience__name":"5년차"} )),
                avg_six         = Avg(f"{key}__salary", filter=Q(**{f"{key}__experience__name":"6년차"} )),
                avg_seven       = Avg(f"{key}__salary", filter=Q(**{f"{key}__experience__name":"7년차"} )),
                avg_eight       = Avg(f"{key}__salary", filter=Q(**{f"{key}__experience__name":"8년차"} )),
                avg_nine        = Avg(f"{key}__salary", filter=Q(**{f"{key}__experience__name":"9년차 이상"} )),
            )[0]

        salary_info = {
                "id"               : job_or_group.id,
                "name"             : job_or_group.name,
                "postingsCount"    : job_or_group.posting_count,
                "avgTotal"         : job_or_group.avg_total,
                "avgZero"          : job_or_group.avg_zero,
                "avgOne"           : job_or_group.avg_one,
                "avgTwo"           : job_or_group.avg_two,
                "avgThree"         : job_or_group.avg_three,
                "avgFour"          : job_or_group.avg_four,
                "avgFive"          : job_or_group.avg_five,
                "avgSix"           : job_or_group.avg_six,
                "avgSeven"         : job_or_group.avg_seven,
                "avgEight"         : job_or_group.avg_eight,
                "avgNine"          : job_or_group.avg_nine,
                "avgArray"         : [
                                        job_or_group.avg_zero,
                                        job_or_group.avg_one,
                                        job_or_group.avg_two,
                                        job_or_group.avg_three,
                                        job_or_group.avg_four,
                                        job_or_group.avg_five,
                                        job_or_group.avg_six,
                                        job_or_group.avg_seven,
                                        job_or_group.avg_eight,
                                        job_or_group.avg_nine
                                    ],
        }

        return JsonResponse({"message":"SUCCESS", "result" : salary_info}, status=200)

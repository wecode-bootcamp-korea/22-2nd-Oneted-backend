from query_debugger import query_debugger
from django.views       import View
from django.http        import JsonResponse

from jobpostings.models import JobGroup, JobPosting, TagCategory
from utils              import authorization, lose_authorization
from users.models       import Bookmark

class TagCategoryView(View):
    @query_debugger
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
        print(tag_categories._prefetch_related_lookups)


        return JsonResponse({"message":"SUCCESS", "result" : tag_category_list}, status=200)
        
class JobGroupView(View):
    @query_debugger
    def get(self, request):
        job_groups     = JobGroup.objects.prefetch_related("job").all()
        print(job_groups.query)
        print(type(job_groups.query))
        job_group_list = [{
                "id"   : job_group.id,
                "name" : job_group.name,
                "jobs" : [{
                    "id"   : job.id,
                    "name" : job.name,
                } for job in job_group.job.all()],
            } for job_group in job_groups]

        return JsonResponse({"message":"SUCCESS", "result" : job_group_list}, status=200)

class PostingDetailView(View):
    @lose_authorization
    @query_debugger
    def get(self, request, posting_id):
        user        = request.user
        job_posting = JobPosting.objects.get(id=posting_id)
        tags        = job_posting.tags.all()
        # ! : select_related 적용
        bookmark    = Bookmark.objects.filter(user=user, job_posting=posting_id).exists()
        job_posting_info={
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
            "tag_info"          : [{
                "name" : tag.name
            } for tag in tags]
        }
        return JsonResponse({"message":"SUCCESS", "result" : job_posting_info}, status=200)

class BookMarkView(View):
    @authorization
    @query_debugger
    def post(self, request, posting_id):
        user = request.user
        job_posting = JobPosting.objects.get(id=posting_id)

        if not Bookmark.objects.filter(user=user, job_posting=job_posting).exists():
            Bookmark.objects.create(
                user        = user,
                job_posting = job_posting
            )
            return JsonResponse({"Check": Bookmark.objects.filter(user=user, job_posting=job_posting).exists()}, status=201)
        Bookmark.objects.get(user=user, job_posting=job_posting).delete()
        return JsonResponse({"Check": Bookmark.objects.filter(user=user, job_posting=job_posting).exists()}, status=201)
from django.views       import View
from django.http        import JsonResponse

from jobpostings.models import JobGroup, TagCategory

class TagCategoryView(View):
    def get(self, request):
        try:
            tag_categories    = TagCategory.objects.prefetch_related("tag").all()
            tag_category_list = [{
                    "id"   : tag_category.id,
                    "name" : tag_category.name,
                    "tags" : [{
                        "id"   : tag.id,
                        "name" : tag.name,
                    } for tag in tag_category.tag.all()],
                } for tag_category in tag_categories]

            return JsonResponse({"message":"SUCCESS", "result" : {"tagCategories" : tag_category_list}}, status=200)
        
        except Exception as e:
            print(e)
            print(e.__class__)
            return JsonResponse({"message":"UNCAUGHT_ERROR"}, status=400)



class JobGroupView(View):
    def get(self, request):
        try:
            job_groups    = JobGroup.objects.prefetch_related("job").all()
            job_group_list = [{
                    "id"   : job_group.id,
                    "name" : job_group.name,
                    "jobs" : [{
                        "id"   : job.id,
                        "name" : job.name,
                    } for job in job_group.job.all()],
                } for job_group in job_groups]

            return JsonResponse({"message":"SUCCESS", "result" : {"jobGroups" : job_group_list}}, status=200)
        
        except Exception as e:
            print(e)
            print(e.__class__)
            return JsonResponse({"message":"UNCAUGHT_ERROR"}, status=400)


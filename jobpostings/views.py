from django.views       import View
from django.http        import JsonResponse

from jobpostings.models import JobGroup

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

        return JsonResponse({"message":"SUCCESS", "result" : {"jobGroups" : job_group_list}}, status=200)
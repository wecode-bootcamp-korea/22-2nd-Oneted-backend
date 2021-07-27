import json
from json.decoder import JSONDecodeError
from utils import authorization
from users.models import User
from django.views       import View
from django.http        import JsonResponse
from django.utils       import timezone

from resumes.models import Resume

class ResumeDetailView(View):
    @authorization
    def get(self, request, resume_id):
        try:
            resume = Resume.objects.get(id=resume_id)
            print(resume)
            if resume.user != request.user:
                return JsonResponse({"message" : "USER_NOT_MATCH"}, status=401)

            result = {
                "title"   : resume.title,
                "isDone"  : resume.is_done,
                "isFile"  : resume.is_file,
                "fileUrl" : resume.file_url,
                "content" : resume.content,
                "user"    : {
                    "name" : request.user.name,
                    "email": request.user.email,
                }
            }
            
            return JsonResponse({"message" : "SUCCESS", "result" : result}, status=200)

        except Resume.DoesNotExist:
            return JsonResponse({"message" : "RESUME_NOT_EXIST"}, status=401)

    @authorization
    def delete(self, request, resume_id):
        try:
            resume = Resume.objects.get(id=resume_id)

            if resume.user != request.user:
                return JsonResponse({"message" : "USER_NOT_MATCH"}, status=401)
            
            resume.delete()
            
            return JsonResponse({"message" : "SUCCESS"}, status=200)
        
        except Resume.DoesNotExist:
            return JsonResponse({"message" : "RESUME_NOT_EXIST"}, status=401)

    @authorization
    def patch(self, request, resume_id):
        try:
            data   = json.loads(request.body)
            resume = Resume.objects.filter(id=resume_id)
            
            if resume[0].user != request.user:
                return JsonResponse({"message" : "USER_NOT_MATCH"}, status=401)

            Resume.objects.filter(id=resume_id).update(
                is_done=data["isDone"],
                title=data["title"],
                content={
                "description" : data["description"],
                "career" : data["career"],
                "education"  : data["education"],
                "skill" : data["skill"],
                },
                updated_at=timezone.now()
            )
            return JsonResponse({"message" : "SUCCESS"}, status=200)

        except JSONDecodeError:
            return JsonResponse({"message" : "JSON_DECODE_ERROR"}, status=400)

        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)

        except IndexError:
            return JsonResponse({"message" : "RESUME_NOT_EXIST"}, status=400)

class ResumeView(View):
    @authorization
    def post(self, request):
        try:
            data = json.loads(request.body)
            Resume.objects.create(
                user=request.user,
                is_done=data["isDone"],
                title=data["title"],
                content={
                "description" : data["description"],
                "career" : data["career"],
                "education"  : data["education"],
                "skill" : data["skill"],
                })
            return JsonResponse({"message" : "SUCCESS"}, status=200)

        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)

        except JSONDecodeError:
            return JsonResponse({"message" : "JSON_DECODE_ERROR"}, status=400)

    @authorization
    def get(self, request):
        resumes = Resume.objects.filter(user=request.user)
        result = [{
                "id"      : resume.id,
                "title"   : resume.title,
                "isDone"  : resume.is_done,
                "isFile"  : resume.is_file,
                "fileUrl" : resume.file_url
            }for resume in resumes]

        return JsonResponse({"message" : "SUCCESS", "result" : result}, status=200)

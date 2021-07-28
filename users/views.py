from resumes.models import Apply
from query_debugger import query_debugger
import jwt
import json
import requests

from django.views  import View
from django.http   import JsonResponse

from users.models       import User, Bookmark
from jobpostings.models import JobPosting
from my_settings        import DATABASES, SECRET_KEY, ALGORITHM
from utils              import authorization

# Create your views here.
class KakaoLoginView(View):
    @query_debugger
    def post(self, request):
        try:
            access_token = request.headers["Authorization"]
            headers      = ({"Authorization": f"Bearer {access_token}"})
            url          = "https://kapi.kakao.com/v2/user/me"
            response     = requests.get(url, headers=headers)
            user         = response.json()

            if not User.objects.filter(kakao_api_id=user["id"]).exists():
                User.objects.create(
                    name          = user["kakao_account"]["profile"]["nickname"],
                    email         = user["kakao_account"]["email"],
                    profile_image = user["kakao_account"]["profile"]["profile_image_url"],
                    kakao_api_id  = user["id"]
                )
            user = User.objects.get(kakao_api_id=user['id'])
            user_info = {
                "name": user.name,
                "email": user.email,
                "profile_image": user.profile_image
            }
            encoded_jwt = jwt.encode({"user_id": user.id}, SECRET_KEY, algorithm=ALGORITHM)

            return JsonResponse({"user_info":user_info, "token":encoded_jwt}, status=201)

        # 예외처리
        except KeyError:
            return JsonResponse({"message" : "GIVE_ME_TOKEN"}, status=400)

# ! : ORM 최적화 필요. 
class UserView(View):
    @authorization
    @query_debugger
    def get(self, request):
        applies   = Apply.objects.select_related("job_posting", "job_posting__experience", "job_posting__company", "job_posting__company__region", "job_posting__company__region__country", "job_posting__job").prefetch_related("resume").filter(user=User.objects.get(id=1))
        user_info = {
            "id"           : request.user.id,
            "name"         : request.user.name,
            "email"        : request.user.email,
            "profileImage" : request.user.profile_image,
            "applies"      : [{
                "targetedPosting" : {
                    "id"         : apply.job_posting.id,
                    "title"      : apply.job_posting.title,
                    "salary"     : apply.job_posting.salary,
                    "experience" : apply.job_posting.experience.name,
                    "imageUrl"   : apply.job_posting.image_url,
                    "company"    : {
                        "id"      : apply.job_posting.company.id,
                        "name"    : apply.job_posting.company.name,
                        "region"  : apply.job_posting.company.region.name,
                        "country" : apply.job_posting.company.region.country.name,
                    },
                    "job"        : {
                        "id"   : apply.job_posting.job.id,
                        "name" : apply.job_posting.job.name,
                    },
                }
            }for apply in applies]
        }

        return JsonResponse({"message":"SUCCESS", "result" : user_info}, status=200)
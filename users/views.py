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

class UserView(View):
    @authorization
    @query_debugger
    def get(self, request):
        user_info = {
            "id" : request.user.id,
            "name" : request.user.name,
            "email" : request.user.email,
            "profileImage" : request.user.profile_image,
        }

        return JsonResponse({"message":"SUCCESS", "result" : user_info}, status=200)
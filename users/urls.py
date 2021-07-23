from django.urls import path
from users.views import KakaoLoginView, UserView
urlpatterns = [
    path('/kakaologin', KakaoLoginView.as_view()),
    path('/info', UserView.as_view()),
]
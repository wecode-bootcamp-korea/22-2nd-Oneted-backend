from django.urls import path

from jobpostings.views import JobGroupView

urlpatterns = [
    path("/jobs", JobGroupView.as_view()),
]
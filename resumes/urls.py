from django.urls import path

from resumes.views import ResumeView, ResumeDetailView

urlpatterns = [
    path("", ResumeView.as_view()),
    path("/<int:resume_id>", ResumeDetailView.as_view()),
]
from django.urls import path

from resumes.views import ResumesView, ResumeDetailView

urlpatterns = [
    path("", ResumesView.as_view()),
    path("/<int:resume_id>", ResumeDetailView.as_view()),
]
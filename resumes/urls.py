from django.urls import path

<<<<<<< HEAD
from resumes.views import ResumesView, ResumeView, ResumeApply
=======
from resumes.views import ResumesView, ResumeView, ResumeFile
>>>>>>> a39cbdfe6a232cbdd71fed7451da4d69f6e33f96

urlpatterns = [
    path("", ResumesView.as_view()),
    path("/<int:resume_id>", ResumeView.as_view()),
<<<<<<< HEAD
    path('/apply', ResumeApply.as_view())
]
=======
    path('/file', ResumeFile.as_view()),
    path('/file/<int:resume_id>', ResumeFile.as_view())
]
>>>>>>> a39cbdfe6a232cbdd71fed7451da4d69f6e33f96

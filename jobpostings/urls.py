from django.urls import path

from jobpostings.views import JobGroupView, TagCategoryView

urlpatterns = [
    path("/tags", TagCategoryView.as_view()),
    path("/jobs", JobGroupView.as_view()),
]
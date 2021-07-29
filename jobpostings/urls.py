from django.urls import path

from jobpostings.views import PostingsView, SalaryView, SuggestView, TagCategoryView, JobGroupView

urlpatterns = [
    path("", PostingsView.as_view()),
    path("/suggested", SuggestView.as_view()),
    path("/tags", TagCategoryView.as_view()),
    path("/jobs", JobGroupView.as_view()),
    path("/salary", SalaryView.as_view()),
]
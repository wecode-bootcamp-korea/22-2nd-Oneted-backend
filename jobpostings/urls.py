from django.urls import path

from jobpostings.views import ApplyView, PostingsView, SuggestView, TagCategoryView, JobGroupView

urlpatterns = [
    path("", PostingsView.as_view()),
    path("/suggested", SuggestView.as_view()),
    path("/tags", TagCategoryView.as_view()),
    path("/jobs", JobGroupView.as_view()),
    path('/<int:posting_id>/apply', ApplyView.as_view()),
]
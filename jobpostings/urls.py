from django.urls import path

from jobpostings.views import BookMarkView, PostingDetailView, PostingsView, SuggestView, TagCategoryView, JobGroupView

urlpatterns = [
    path("", PostingsView.as_view()),
    path("/suggested", SuggestView.as_view()),
    path("/tags", TagCategoryView.as_view()),
    path("/jobs", JobGroupView.as_view()),
    path('/<int:posting_id>/bookmark', BookMarkView.as_view()),
    path('/<int:posting_id>', PostingDetailView.as_view()),
]
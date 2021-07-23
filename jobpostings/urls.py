from django.urls import path

from jobpostings.views import BookMarkView, PostingDetailView, TagCategoryView, JobGroupView

urlpatterns = [
    path("/tags", TagCategoryView.as_view()),
    path("/jobs", JobGroupView.as_view()),
    path('/<int:posting_id>/bookmark', BookMarkView.as_view()),
    path('/<int:posting_id>', PostingDetailView.as_view()),
]
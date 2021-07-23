from django.urls import path

from search.views import SearchView, SuggestView

urlpatterns = [
    path("", SearchView.as_view()),
    path("/suggested", SuggestView.as_view()),
]
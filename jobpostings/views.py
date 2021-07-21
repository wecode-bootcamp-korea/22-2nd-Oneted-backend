from jobpostings.models import TagCategory
from django.views       import View

class TagView(View):
    def get(self, request):
        print(request)
        # select related
        tag_categories = TagCategory.objects.select_all()
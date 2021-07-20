from django.db import models

# Create your views here.
class User(models.Model):
    name          = models.CharField(max_length = 20)
    email         = models.EmailField(max_length = 100, unique = True)
    phone_number  = models.CharField(max_length = 100)
    profile_image = models.ImageField(null = True)
    created_at    = models.DateTimeField(auto_now_add = True)
    updatad_at    = models.DateTimeField(auto_now = True)

    class Meta :
        db_table = "users"

class Platforms(models.Model):
    name = models.CharField(max_length = 45)

    class Meta:
        db_table = "platforms"

class UsersPlatforms(models.model):
    platform_user_id = models.CharField(max_length = 100)
    users            = models.ForeignKey(User, on_delete=models.CASCADE)
    platform         = models.ForeignKey(Platforms, on_delete=models.CASCADE)

    class Meta :
        db_table = "users_platforms"

class Bookmark(models.Model):

    class Meta :
        db_table = "bookmarks"

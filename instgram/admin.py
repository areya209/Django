from django.contrib import admin
from .models import Post, Profile, Follow, Comment, Likes

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Follow)
admin.site.register(Comment)
admin.site.register(Likes)

# Register your models here.

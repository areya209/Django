from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


# Create your models here.
class Profile(models.Model):
    bio = models.CharField(max_length=300, blank=True, default='Awesome Bio Will Appear Here')
    profile_pic = models.ImageField(upload_to='profile/', blank=True, default='../static/images/default.png')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    image_name = models.CharField(max_length=60, blank=True)
    image_caption = models.CharField(max_length=60, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(User, related_name='post', on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="likes", blank=True)
    image = models.ImageField(upload_to='images/', blank=True)

    @classmethod
    def save_image(self):
        self.save()

    @classmethod
    def delete_image(self):
        self.delete()

    @classmethod
    def get_image_by_id(cls, image_id):
        image = cls.objects.get(id=image_id)
        return image

    def total_likes(self):
        self.likes.count()

    def __str__(self):
        return self.profile.username


class Comment(models.Model):
    comment = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ForeignKey(Post, related_name="comment", on_delete=models.CASCADE)
    profile = models.ForeignKey(User, related_name="comment", on_delete=models.CASCADE)

    def __str__(self):
        return self.profile.username


class Follow(models.Model):
    user_from = models.ForeignKey(User, related_name='follow', on_delete=models.CASCADE)
    user_to = models.ForeignKey(User, related_name='folllow', on_delete=models.CASCADE)

    def __str__(self):
        return '{} follows {}'.format(self.user_from, self.user_to)


User.add_to_class('following',
                  models.ManyToManyField('self',
                                         through=Follow,
                                         related_name='followers',
                                         symmetrical=False))


class Col(models.Model):
    addtest = models.FileField()


# Class Like
class Likes(models.Model):
    user_like = models.ForeignKey(User, related_name='ulikes', on_delete=models.CASCADE)
    post_like = models.ForeignKey(Post, related_name='plikes', on_delete=models.CASCADE)

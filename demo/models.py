from django.contrib.auth.forms import UserCreationForm
from django.db import models

# class Registration(models.Model):
#     Firstname  = models.CharField(max_length=50,unique=True)
#     Lastname = models.CharField(max_length=50, unique=True)
#     Email  = models.CharField(max_length=50, unique=True)
#     Password = models.IntegerField(max_length=30)
#     Mobilephone = models.IntegerField(max_length=30)
#     ProfilePicture = models.ImageField(upload_to='cars')

# Create your models here.


from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Board(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)



class Topic(models.Model):
    subject = models.CharField(max_length=255)
    board = models.ForeignKey(Board,related_name='topics',on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,related_name='topics',on_delete=models.CASCADE)
    created_dt = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic,related_name='posts',on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
    created_dt = models.DateTimeField(auto_now_add=True)

# class NewUserForm(UserCreationForm):
# 	email = forms.EmailField(required=True)
#
# 	class Meta:
# 		model = User
# 		fields = ("username", "email", "password1", "password2")



class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)

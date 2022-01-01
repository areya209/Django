from django.contrib.auth.models import User

from django.shortcuts import render

# Create your views here.
from django.template.context_processors import request
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from knox.models import AuthToken
from django.contrib.auth import login

from rest_framework import permissions, status, filters
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

from instgram.api import Commentadd, POSRSIL, USerview, viewprofile, viewfollow, ADD, ChangePasswordSerializer, \
    ProfileSer, viewlike
from instgram.models import Comment, Post, Profile, Follow, Col, Likes

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework.permissions import IsAuthenticated


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# all comment
@api_view(['GET'])
def get(request):
    queryset = Comment.objects.all()
    data = Commentadd(queryset, many=True).data
    return Response(data)


@api_view(['GET'])
def AuthApi(request):
    user = request.user
    return Response('Auth')


@api_view(['GET'])
def getuser(request):
    queyset = User.objects.all()
    data = USerview(queyset, many=True).data
    return Response(data)


# all post
class Dataview(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = POSRSIL


# all post
class Addt(generics.ListCreateAPIView):
    queryset = Col.objects.all()
    serializer_class = ADD


# view post id
class Dataid(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = POSRSIL
    Lookup_field = 'pk'


# Update personal data Of User
class Viewuser(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = USerview
    Lookup_field = 'pk'


class Viewuserall(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = USerview


class Viewpprofile(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = viewprofile
    Lookup_field = 'pk'


class Viewpprofile2(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = viewprofile
    Lookup_field = 'pk'


class Viewfolloww(generics.RetrieveUpdateDestroyAPIView):
    queryset = Follow.objects.all()
    serializer_class = viewfollow
    Lookup_field = 'pk'


@api_view(['GET'])
def getp(request, id_user):
    queryset = Post.objects.filter(profile=id_user).order_by('-created_at')
    data = POSRSIL(queryset, many=True).data
    return Response(data)


@api_view(['GET'])
def getprofile(request, id_user):
    queryset = Profile.objects.filter(user=id_user)
    data = viewprofile(queryset, many=True).data
    return Response(data)


# Add my profile picture By uploaded it
class Addprofilephoto(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = viewprofile


# Limit Only 5 Users
@api_view(['GET'])
def limitusers(request):
    queyset = User.objects.all().order_by('-id')[:15]
    data = USerview(queyset, many=True).data
    return Response(data)


@api_view(['GET'])
def getfollowing(request, id):
    queryset = Follow.objects.filter(user_from=id)
    data = viewfollow(queryset, many=True).data
    return Response(data)


@api_view(['GET'])
def getfollowers(request, id):
    queryset = Follow.objects.filter(user_to=id)
    data = viewfollow(queryset, many=True).data
    return Response(data)


class follow(generics.ListCreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = viewfollow


# Update the Profile Of User (Picture, Bio)
class ProfileUpdate(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSer
    Lookup_field = 'user'


# Add Comment On the Post
class Addcomment(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = Commentadd


@api_view(['GET'])
def getcomment(request, id_post):
    queryset = Comment.objects.filter(image=id_post)
    data = Commentadd(queryset, many=True).data
    return Response(data)


# Add Only Followers to Login User
@api_view(['GET'])
def getfollowe(request, id_user):
    so = Follow.objects.filter(user_from=id_user)
    data = viewfollow(so, many=True).data
    print(data)
    if data:
        # ser = POSRSIL(data, many=True)
        x = []
        for k in data:
            x.append(k['user_to'])
        print(x)
        filterfin = Post.objects.filter(profile__in=x)
        print(filterfin)
        ser = POSRSIL(filterfin, many=True)
        x = []
        print(x)
        return Response(ser.data)

    else:
        return Response('None')


# UnFollow Follow
@api_view(["DELETE"])
def delfollowers(request, *args, **kwargs):
    p = request.data.get('user_from')
    print(request.data.get('user_from'))
    c = request.data.get('user_to')
    queryset = Follow.objects.get(user_from=p, user_to=c).delete()
    data = viewfollow(queryset, many=True).data
    return Response(data)


# Delete Post
@api_view(["DELETE"])
def delpost(request):
    p = request.data.get('id')
    c = request.data.get('profile')
    queryset = Post.objects.get(id=p, profile=c).delete()
    data1 = POSRSIL(queryset, many=True).data
    return Response(data1)


# Delete Comment
@api_view(["DELETE"])
def delcomment(request):
    i = request.data.get('id')
    c = request.data.get('profile')
    e = request.data.get('image')
    queryset = Comment.objects.get(id=i, profile=c, image=e).delete()
    data1 = Commentadd(queryset, many=True).data
    return Response(data1)


# view Of Like
class like(generics.ListCreateAPIView):
    queryset = Likes.objects.all()
    serializer_class = viewlike


# Get Likes
@api_view(['GET'])
def getlike(request, id):
    queryset = Likes.objects.filter(post_like=id)
    data = viewlike(queryset, many=True).data
    return Response(data)


# Delete Like
@api_view(["DELETE"])
def dellike(request):
    p = request.data.get('user_like')
    c = request.data.get('post_like')
    queryset = Likes.objects.get(user_like=p, post_like=c).delete()
    data1 = viewlike(queryset, many=True).data
    return Response(data1)


# Reset Password Of User
class ChangePasswordView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer

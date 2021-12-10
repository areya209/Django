from django.shortcuts import render

# Create your views here.
from django.template.context_processors import request
from rest_framework import generics

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User


from instgram.api import Commentadd, POSRSIL, USerview, viewprofile, viewfollow
from instgram.models import Comment, Post, Profile, Follow


# @api_view(['GET','POST'])
# class Apostudent(request):
#     def get(self,requset):
#         queryset = Post.objects.all()
#         data = Studentser(queryset,many=True).data
#         return Response(data)
#     def set(self,request):
#         silzer = Studentser(data=request.data)
#         if silzer.is_valid():
#             silzer.save()
#             return Response(silzer.data)
# all comment
@api_view(['GET'])
def get(request):
    queryset = Comment.objects.all()
    data = Commentadd(queryset, many=True).data
    return Response(data)

# all post
class Dataview(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = POSRSIL

# view post id
class Dataid(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = POSRSIL
    Lookup_field = 'pk'



class Viewuser(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = USerview
    Lookup_field = 'pk'


class Viewpprofile(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = viewprofile
    Lookup_field = 'pk'


class Viewfolloww(generics.RetrieveUpdateDestroyAPIView):
    queryset = Follow.objects.all()
    serializer_class = viewfollow
    Lookup_field = 'pk'
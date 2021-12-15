from django.contrib.auth.models import User

from django.shortcuts import render

# Create your views here.
from django.template.context_processors import request
from rest_framework import generics
from rest_framework.authtoken.models import Token

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from knox.models import AuthToken
from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView


from instgram.api import Commentadd, POSRSIL, USerview, viewprofile, viewfollow, ADD
from instgram.models import Comment, Post, Profile, Follow, Col


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

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


class Viewfolloww(generics.RetrieveUpdateDestroyAPIView):
    queryset = Follow.objects.all()
    serializer_class = viewfollow
    Lookup_field = 'pk'


#
# # Register API
#
#
#
# class RegisterAPI(generics.GenericAPIView):
#     serializer_class = USerview
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         return Response({
#         "user": USerview(user, context=self.get_serializer_context()).data,
#         "token": AuthToken.objects.create(user)[1]
#         })
#
#
# class LoginAPI(KnoxLoginView):
#     permission_classes = (permissions.AllowAny,)
#
#     def post(self, request, format=None):
#         serializer = AuthTokenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         login(request, user)
#         return super(LoginAPI, self).post(request, format=None)
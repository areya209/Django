"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from instgram import views
from .views import TokenObtainPairView

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from .views import ChangePasswordView

urlpatterns = [
    # path('apis', views.Apostudent.as_view() ,name="api"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('get', views.get, name="f"),
    path('Posts/', views.Dataview.as_view(), name='Data'),
    path('postid/<int:pk>', views.Dataid.as_view(), name="ff"),
    path('userid/<int:pk>', views.Viewuser.as_view()),
    path('userall/', views.Viewuserall.as_view(), name="usera"),
    path('addd', views.Addt.as_view()),
    # path('register/', views.RegisterAPI.as_view(), name='register'),
    path('Authapi/', views.AuthApi, name='Authapi'),
    path('getp/<int:id_user>', views.getp, name="fp"),
    path('profile2/<int:pk>', views.Viewpprofile2.as_view()),
    path('profile/<int:pk>', views.Viewpprofile.as_view()),
    path('viewfollow/<int:pk>', views.Viewfolloww.as_view()),
    path('follow/', views.follow.as_view()),
    path('getprofile/<int:id_user>', views.getprofile),
    path('limitusers/', views.limitusers),
    path('getfollowing/<int:id>', views.getfollowing),
    path('getfollowers/<int:id>', views.getfollowers),
    path('getprofile/<int:id_user>', views.getprofile),
    path('limitusers/', views.limitusers),
    path('addphoto/', views.Addprofilephoto.as_view(), name='Addprofile'),
    path('update/<int:pk>', views.ProfileUpdate.as_view(),name="ProfileUpdate"),
    path('addcomment/', views.Addcomment.as_view()),
    path('getcomment/<int:id_post>', views.getcomment),
    path('viewfollowers/<int:id_user>', views.getfollowe),
    path('delfollowers/',views.delfollowers),
    path('delpost/', views.delpost),
    path('delcomment/', views.delcomment),
    path('like/',views.like.as_view()),
    path('getlike/<int:id>',views.getlike),
    path('dellike/',views.dellike),


]

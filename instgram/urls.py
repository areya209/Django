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

urlpatterns = [
    # path('apis', views.Apostudent.as_view() ,name="api"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('get',views.get,name="f"),
    path('Posts/',views.Dataview.as_view(),name='Data'),
    path('postid/<int:pk>',views.Dataid.as_view(),name="ff"),
    path('userid/<int:pk>',views.Viewuser.as_view()),
    path('userall/', views.Viewuserall.as_view(),name="usera"),
    path('addd',views.Addt.as_view()),
    # path('register/', views.RegisterAPI.as_view(), name='register'),
    path('Authapi/', views.AuthApi, name='Authapi'),

    path('profile/<int:pk>',views.Viewpprofile.as_view()),
    path('viewfollow/<int:pk>',views.Viewfolloww.as_view())

    # path('demo',include('demo.url')),
    # path('', views.home),
    # path('projectadd',views.Projectadd,name='projectadd2'),
    # path('viewprojects',views.viewproject,name='viewprojects1'),
    # path('idproject/<int:id>/',views.viewid,name='viewidd'),
    # path('apis',views.Apostudent.as_view(),name='apis')
]

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
from django.urls import path,include
from . import views
from django.contrib.auth import views  as outhn
from demo import views
urlpatterns = [

    # path('demo',include('demo.url')),
    path('hamed/', views.home),
    path('del/<int:st_id>/',views.detils ,name='detils'),
    path('name/<str:st_name>/', views.detil, name='detil'),
    path('na', views.signup, name='sign'),
    # path('', views.login, name='de'),
    path('logut',views.logOut , name='logut'),
    path('viewuser',views.viewuser,name='vewiu'),
    path('login',views.loginbase ,name='login'),
    path('',outhn.LoginView.as_view(template_name='demo/login.html'),name='log'),
    path('settings/passwors/',outhn.PasswordChangeView.as_view(template_name='demo/chanche.html'),name='chan')
    # path('', views.index, name='index'),
# path('<str:room_name>/', views.room, name='room'),
]

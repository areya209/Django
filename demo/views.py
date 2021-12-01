from .models import Board
from .forms import Userauth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as loginauth,logout as logoutsite,authenticate
from django.shortcuts import render, redirect

from .forms  import SignUpForm,User
# Create your views here.
def home(request):

    # Board.objects.create(name='mohamednour',description='UI UX')
    form = Board.objects.all()
    return render(request, 'demo/home.html', {'form': form})


def logOut(request):
    logoutsite(request)

    return render(request,'demo/logotsite.html')
@login_required
def detils(request,st_id):

    # Board.objects.create(name='mohamednour',description='UI UX')
    form = Board.objects.filter(id=st_id)
    return render(request, 'demo/id.html', {'form': form})
def viewuser(request):

    return render(request, 'demo/viewuser.html')

def detil(request,st_name):

    # Board.objects.create(name='mohamednour',description='UI UX')
    form = Board.objects.filter(name=st_name)
    return render(request, 'demo/name.html', {'form': form})

# def index(request):
#     return render(request, 'demo/chat.html', {})
#
#
# def room(request, room_name):
#     return render(request, 'demo/chat.html', {
#         'room_name': room_name
#     })


# @login_required
# def login(request):
#     return render(request, 'demo/login.html')



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user =   form.save()
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # # first_name = form.cleaned_data.get('first_name')
            # # last_name = form.cleaned_data.get('last_name')
            # # email = form.cleaned_data.get('email')
            # # mobile = form.cleaned_data.get('mobile')
            # user = authenticate(username=username, password=raw_password)
            # # User.objects.create(first_name=first_name,last_name=last_name,email=email,mobile=mobile)

            loginauth(request, user)
            return redirect('hamed/')
    else:
        form = SignUpForm()
    return render(request, 'demo/signup.html', {'form': form})


def loginbase(request):
    form = Userauth
    if (request.method == 'GET'):
        return render(request, 'demo/login.html', {'form': form})
    else:
       user = authenticate(username=request.POST['username'],password=request.POST['password'])
       print(user)
       if (user):
           loginauth(request,user)
           return redirect('hamed/')
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Projects, Projectcomments, Projectpictures, Commentsreport
from .forms import Addproject
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods


# Create your views here
# @login_required
def home(request):
    return render(request, 'project/base.html')


def viewproject(request):
    dataproject = Projects.objects.all()

    return render(request, 'project/viewproject.html', {'data': dataproject})
def viewid(request,id):
    dataproject = Projects.objects.filter(Project_id=id)

    return render(request,'project/showproject.html',{'data':dataproject})

@login_required
def Projectadd(request):
    form = Addproject
    if (request.method == 'GET'):
        return render(request, 'project/Addproject.html', {'form': form})
    else:
        form = Addproject(request.POST)
        if form.is_valid():
            Projects.objects.create(
                Project_name=request.POST['Title'],
                Project_details=request.POST['Details'],
                Total_target=request.POST['Totaltarget'],
                Total_donations=request.POST['Totaldonations'],
                start_date=request.POST['StartDate'],
                end_date=request.POST['EndDate'],
                Avg_rate=request.POST['Rate'],
                # user=request.POST['Owner'],
                # category=request.POST['category']
            )

            return redirect('viewprojects1')

    return render(request, 'project/Addproject.html', {'form': form})

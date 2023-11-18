from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def HODLogin(request):
    return render(request,'HOD/login.html',{})

@login_required(login_url='/HODLogin')
def HOD(request):
    return HttpResponse('this is hod page')
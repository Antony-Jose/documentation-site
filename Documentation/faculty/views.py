from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def facultyLogin(request):
    return render(request,'faculty/login.html',{})

@login_required(login_url='/facultyLogin')
def faculty(request):
    return HttpResponse('this is the faculty page')
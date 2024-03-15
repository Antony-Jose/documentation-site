from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from faculty.models import mfrequest

# Create your views here.
@login_required(login_url='/HODLogin')
def HOD(request):
    return render(request, 'HOD/home.html')
def approved(request):
    return render(request, 'HOD/approved.html')
def rejected(request):
    return render(request, 'HOD/rejected.html')
def hhistory(request):
    return render(request, 'HOD/history.html')

def hnotifications(request):
    reciver = request.user
    all_status = mfrequest.objects.filter(reciver=reciver)
    return render(request, 'HOD/notifications.html',{'status': all_status})

def HODLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # User is valid, log them in
            login(request, user)
            return render(request, 'HOD/home.html')  # Replace 'home' with the URL you want to redirect to after successful login
        else:
            # Invalid login credentials
            return render(request, 'HOD/login.html', {'error_message': 'Invalid username or password'})
 
    return render(request, 'HOD/login.html')

def hlogout(request):
    logout(request) 
    return HODLogin(request)

def HodViewer(request):
    return render(request,'HOD/review.html')
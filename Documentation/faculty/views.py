
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login
from django.shortcuts import render

# Create your views here.


@login_required(login_url='/facultyLogin')
def faculty(request):
    return render(request, 'faculty/home.html')



def facultyLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # User is valid, log them in
            login(request, user)
            return render(request, 'faculty/home.html')  # Replace 'home' with the URL you want to redirect to after successful login
        else:
            # Invalid login credentials
            return render(request, 'faculty/login.html', {'error_message': 'Invalid username or password'})

    return render(request, 'faculty/login.html')

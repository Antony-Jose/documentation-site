
from django.contrib.auth.decorators import login_required
from .models import mfrequest
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.contrib.auth.models import User,Group

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas



# Create your views here.


@login_required(login_url='/facultyLogin')
def faculty(request):
    return render(request, 'faculty/home.html')
def frequest(request):
    if request.method == 'POST':
        sender = request.user
        print(sender)
        groups = sender.groups.all()
        departmentName = groups.first().name if groups.exists() else None
        #departmentName = User.groups.('name',flat=True).first()
        print(departmentName)
        hod_users=User.objects.filter(groups__name='HOD')
        print(hod_users)
        reciver = hod_users.filter(groups__name=departmentName).first()
        print(reciver)
        semes = request.POST["sem"] # request.POST.get('sem')
        subject = request.POST.get('subject')
        body = request.POST.get('body')
        print('subject is ',semes)
        mfrequest(sender=sender,reciver=reciver,sem=semes,subject=subject,body=body).save()
    return render(request,'faculty/request.html')
def fhistory(request):
    return render(request,'faculty/history.html')

def fnotifications(request):
    sender = request.user
    all_status = mfrequest.objects.filter(sender=sender)
    return render(request,'faculty/notifications.html',{'status': all_status})

def fstatus(request):
    return render(request,'faculty/status.html')
def fdownload(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 10, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename="hello.pdf")
    








def flogout(request):
    logout(request) 
    return facultyLogin(request)


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

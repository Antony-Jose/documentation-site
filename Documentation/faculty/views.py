
from django.contrib.auth.decorators import login_required
from .models import mfrequest
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.contrib.auth.models import User,Group
from django.http import HttpResponse

import io
from django.http import FileResponse

def home(request):
    return render(request,'faculty/index.html')




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


def fViewer(request,object_id):
    object = mfrequest.objects.get(pk=object_id)
    return render(request,'faculty/review.html',{'stat':object})


import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Paragraph
from django.http import FileResponse
from .models import mfrequest  # Assuming mfrequest is the model you're using

def fdownload(request, object_id):
    sender = request.user
    print(sender)
    groups = sender.groups.all()
    departmentName = groups.first().name if groups.exists() else None
    obj = mfrequest.objects.get(pk=object_id)
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    p.translate(inch, inch)

    # Drawing lines and images
    p.setStrokeColorRGB(1, 0, 0)
    p.setLineWidth(10)
    p.line(0, 8*inch, 7*inch, 8*inch)
    p.drawImage('faculty/static/profile2.png', 0.8*inch, 7.3*inch)
    p.setFillColor('green')
    p.drawString(100, 725, "From,")
    p.drawString(125, 500, f" {sender.first_name} {sender.last_name}")
    p.drawString(125, 550, str(departmentName))
    p.drawString(100, 525, "To,")
    p.drawString(128, 400, f" {obj.reciver.first_name} {obj.reciver.last_name}")
    p.drawString(125, 560, str(departmentName))
    p.drawString(300, 300, f"Subject: {obj.subject}")
    p.drawString(300, 280, f"Semester: {obj.sem}")

    # Adding paragraph text
    text = obj.body.replace('\n', '<br/>')
    paragraph = Paragraph(text, style=None)  # Adjust properties
    paragraph.wrapOn(p, 400, 300)  # Wrap the paragraph if needed
    paragraph.drawOn(p, 100, 200)  # Draw the paragraph on the canvas

    # Close the PDF object cleanly
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers present the option to save the file
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename="hello.pdf")


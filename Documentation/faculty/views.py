
from django.contrib.auth.decorators import login_required
from .models import mfrequest
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.contrib.auth.models import User,Group
from django.http import HttpResponse

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas #working
"""
from django.template.loader import render_to_string
from weasyprint.html import render_pdf #some dependencies missing
"""






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




"""
def generate_pdf(request):
    template_name = 'pdf.html'
    context = {'data': request.user}
    html_content = render_to_string(template_name, context)
    pdf_response = render_pdf(html_content)
    return HttpResponse(pdf_response, content_type='application/pdf')
"""
def fdownload(request,object_id):
    reciver = request.user
    obj = mfrequest.objects.get(pk=object_id)
    body = obj.body
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()
    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 500, f"{request.user}")
    p.drawString(100, 400, f"{ obj.reciver }")
    p.drawString(100, 300, f"{ obj.sem }")
    p.drawString(100, 200, f"{ obj.body }")
    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename="hello.pdf")
    


# Django view
from django.template import loader
from django.core.files.base import ContentFile

def generate_pdf(request,object_id):
    object = mfrequest.objects.get(pk=object_id)
    context = {'from': request.user, }
    loader.get_template('faculty/pdf.html')
    pdf = generate_report(context)  # Call your Reportlab function here
    response = FileResponse(ContentFile(pdf), content_type='application/pdf')
    #response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="pdf.pdf"'
    return response

def generate_report(context):
    faculty = context['from']
    order_id = context['order_id']
    c = canvas.Canvas('letter.pdf')
    
    c.drawString(100, 100, f"Customer Name: {faculty}")
    c.drawString(100, 80, f"Order ID: {order_id}")
    c.drawString(100, 200, " H e l  l  o world.")
    # ... (add more elements)
    c.save()
    with open("letter.pdf", 'rb') as f:
      pdf_data = f.read()
    return pdf_data  # Return the PDF data as bytes


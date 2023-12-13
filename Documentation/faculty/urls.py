
from django.urls import path
from . import views

urlpatterns = [
    path('faculty/',views.faculty,name="fhome"),
    path('facultyLogin/',views.facultyLogin,name="flogin"),
    path('faculty/frequest',views.frequest,name="frequest"), 
    path('faculty/fhistory',views.fhistory,name="fhistory"),
    path('faculty/fstatus',views.fstatus,name="fstatus"),
    path('faculty/fnotifications',views.fnotifications,name="fnotifications"),
    

    
]
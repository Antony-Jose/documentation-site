
from django.urls import path
from . import views

urlpatterns = [
    path('faculty/',views.faculty),
    path('facultyLogin/',views.facultyLogin),
    path('faculty/frequest',views.frequest), 
    path('faculty/fhistory',views.fhistory),
    path('faculty/fstatus',views.fstatus),
    path('faculty/fnotifications',views.fnotifications),
    

    
]
from django.urls import path
from . import views

urlpatterns = [
    path('HOD/',views.HOD),
    path('HODLogin/',views.HODLogin),
    path('HOD/frequest',views.frequest), 
    path('HOD/fhistory',views.fhistory),
    path('HOD/fstatus',views.fstatus),
    path('HOD/fnotifications',views.fnotifications),
    
]
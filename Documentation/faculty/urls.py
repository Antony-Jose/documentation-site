
from django.urls import path
from . import views

urlpatterns = [
    path('faculty/',views.faculty),
    path('facultyLogin/',views.facultyLogin),
    
]
from django.urls import path
from . import views

urlpatterns = [
    path('HOD/',views.HOD),
    path('HODLogin/',views.HODLogin),
]
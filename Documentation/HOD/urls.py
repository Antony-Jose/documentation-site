from django.urls import path
from . import views

urlpatterns = [
    path('HOD/',views.HOD,name="hhome"),
    path('HODLogin/',views.HODLogin,name="hlogin"),
    path('HOD/approved',views.approved,name="happrove"), 
    path('HOD/rejected',views.rejected,name="hreject"),
    
]
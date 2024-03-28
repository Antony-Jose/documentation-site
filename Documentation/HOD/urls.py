from django.urls import path
from . import views

urlpatterns = [
    path('HOD/',views.HOD,name="hhome"),
    path('HODLogin/',views.HODLogin,name="hlogin"),
    path('HOD/approved',views.approved,name="happrove"), 
    path('HOD/rejected',views.rejected,name="hreject"),
    path('HOD/history',views.hhistory,name="hhistory"),
    path('HOD/notifications',views.hnotifications,name="hnotifications"),
    path('HOD/notifications/<int:object_id>/',views.evaluate,name="evaluate"),
    path('HOD/review/<int:object_id>/',views.HodViewer,name="viewer"),
    path('HODLogout/',views.hlogout,name="hlogout"),   
]
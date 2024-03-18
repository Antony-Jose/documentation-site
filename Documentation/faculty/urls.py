
from django.urls import path
from . import views

urlpatterns = [
    path('faculty/',views.faculty,name="fhome"),
    path('facultyLogin/',views.facultyLogin,name="flogin"),
    path('faculty/frequest',views.frequest,name="frequest"), 
    path('faculty/fhistory',views.fhistory,name="fhistory"),
    path('faculty/fstatus',views.fstatus,name="fstatus"),
    path('faculty/fnotifications',views.fnotifications,name="fnotifications"),
    path('faculty/fdownload/<int:object_id>/',views.fdownload,name="fdownload"),
    path('facultyLogout',views.flogout,name="flogout"),
    path('faculty/pdf',views.fdownload,name="pdf"),
    path('faculty/review/<int:object_id>/',views.fViewer,name="fviewer"),
]
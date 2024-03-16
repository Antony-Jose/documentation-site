from django.db import models
from django.contrib.auth.models import User,AbstractUser,Group


# Create your models here.


class mfrequest(models.Model):
    
    sender = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    reciver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='HOD',blank=True,null=True)
    sem = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    body = models.TextField()
    checked = models.BooleanField(default=False)
    permitted = models.BooleanField(default=False)
    remarks = models.TextField(default='NO REMARKS')
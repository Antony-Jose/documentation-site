from django.db import models

# Create your models here.
class mfrequest(models.Model):
    sem = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    body = models.TextField()

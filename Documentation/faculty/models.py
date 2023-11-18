from django.db import models

# Create your models here.
class request(models.Model):
    sender = models.CharField(max_length=20)
    #dept = models. use dropdown ?
    #date automatic or manual ?? 
    subject = models.CharField(max_length=100)
    bodu = models.TextField
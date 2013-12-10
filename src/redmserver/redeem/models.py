from django.db import models

# Create your models here.
class RedeemRecord(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    redmcode = models.CharField(max_length=8)
    redmbit = models.CharField(max_length=1)
    gift = models.CharField(max_length=20)
        
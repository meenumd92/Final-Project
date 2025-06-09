from django.db import models

# Create your models here.



class Vendor(models.Model):
    company_name = models.CharField(max_length=100)
    password = models.CharField(default=0)
    email = models.EmailField()  

class PackReg(models.Model):
    amount = models.IntegerField(null=True)
    package =models.TextField(max_length=500)
    days = models.IntegerField(null=True)
    img = models.ImageField(upload_to='gallery/' ,null=True)
    approval = models.BooleanField(default=False)


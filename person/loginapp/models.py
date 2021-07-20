from django.db import models

# Create your models here.
class Details(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    username=models.CharField(max_length=30,null=True)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=20)
    address=models.CharField(max_length=100,null=True)
    state=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    choices=[('Doctor','Doctor'),('Patient','Patient')]
    pincode=models.CharField(max_length=10,default='0')
    typeofperson=models.CharField(choices=choices,max_length=10)

    def __str__(self):
       return  self.email
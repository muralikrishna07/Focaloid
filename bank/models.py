from django.db import models

# Create your models here.
class account(models.Model):
    name=models.CharField(max_length=120)
    accno=models.CharField(max_length=15)
    mpin=models.CharField(max_length=6,unique=True)
    email=models.EmailField(max_length=20)
    phonenumber=models.CharField(max_length=12)
    balance=models.IntegerField(default=3000)
    
    def __str__(self):
        return self.name  


class Transferdetails(models.Model):
    mpin=models.CharField(max_length=6)
    accno=models.CharField(max_length=15)
    amount=models.IntegerField()

    def __str__(self):
        return self.mpin+ self.accno
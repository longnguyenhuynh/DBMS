from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class user(models.Model):
    username = models.CharField(max_length=16, primary_key=True)
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=10)

class customer(models.Model):
    username = models.ForeignKey(user, on_delete=models.CASCADE)
    balanced = models.IntegerField(auto_created=0)

class staff(models.Model):
    username = models.ForeignKey(user, on_delete=models.CASCADE)

class manager(models.Model):
    username = models.ForeignKey(user, on_delete=models.CASCADE)

class ITStaff(models.Model):
    username = models.ForeignKey(user, on_delete=models.CASCADE)





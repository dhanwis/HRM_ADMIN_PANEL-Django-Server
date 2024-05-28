from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser): 
    is_user = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_teamlead = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_frontoffice = models.BooleanField(default=False)
    is_intern = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=12,null=True,blank=True)
    address = models.CharField(max_length=100,null=True,blank=True)
    dob = models.DateField(auto_now=False, auto_now_add=False,null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    state = models.CharField(max_length=30,null=True,blank=True)
    country = models.CharField(max_length=20,null=True,blank=True)
    image = models.ImageField(upload_to="user",null=True,blank=True)
    pincode = models.CharField(max_length=8,null=True,blank=True)
    role = models.CharField(max_length=20,null=True,blank=True)
    department =models.CharField(max_length=40,null=True,blank=True)
    experience = models.CharField(max_length=100,null=True,blank=True)
    
    
class UserProfile(models.Model):
    user = models.OneToOneField(User,models.CASCADE)
    university = models.CharField(max_length=100)
    degree_program = models.CharField(max_length=100)
    internship_position = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    intership_type = models.CharField(max_length=50)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    stipend_amount = models.DecimalField(max_digits=10,decimal_places=2)
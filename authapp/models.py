from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser): 
    is_hr= models.BooleanField(default=False)
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
    image = models.ImageField(upload_to="user/",null=True,blank=True)
    pincode = models.CharField(max_length=8,null=True,blank=True)
    role = models.CharField(max_length=20,null=True,blank=True)
    department =models.CharField(max_length=40,null=True,blank=True)
    experience = models.CharField(max_length=100,null=True,blank=True)
    
    
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    educationalQualification= models.CharField(max_length=100)
    course = models.CharField(max_length=100,unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    category_choices = (
        ("Student", "Student"),
        ("Product", "Product")
    )
    category = models.CharField(choices=category_choices, max_length=20, default=1)
    payment_option_choices = (
        ("Total Amount", "Total Amount"),
        ("Installment", "Installment")
    )
    payment = models.CharField(choices=payment_option_choices, max_length=20, default=1)
    payment_date = models.DateField(null=True, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    no_of_installments = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.user.username
    def __str__(self):
        return self.course
    

class Reference(models.Model):      
    name=models.CharField(max_length=100, null=True,blank=True)
    email=models.CharField(max_length=100,null=True,blank=True)
    phone = models.CharField(max_length=100, null=True,blank=True)
    location =  models.CharField(max_length=100, null=True,blank=True)
    education =  models.CharField(max_length=100, null=True,blank=True)

    def _str_(self):
        return self.name   
    
    
class Feedback(models.Model):
    feedback = models.CharField(max_length=500,null=True,blank=True)
    
class Testimonial(models.Model):
    testimonial = models.CharField(max_length=500,null=True,blank=True)

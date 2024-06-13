from django.db import models
from authapp.models import User
# Create your models here.


class TeamleadAssign(models.Model):
    user = models.ForeignKey(User,models.CASCADE,limit_choices_to={'is_teamlead':True})
    tasktitle = models.CharField(max_length=100)
    startdate = models.DateField(max_length=100,null=True,blank=True)
    enddate = models.DateField(max_length=100,null=True,blank=True)
    task_description = models.CharField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return self.user.username
    
class StudentAssign(models.Model):
    student_name=models.ForeignKey(User,models.CASCADE,limit_choices_to={'is_intern':True},to_field='username')
    task_name=models.CharField(max_length=100,null=True,blank=True)
    task_details=models.CharField(max_length=100,null=True,blank=True)
    guide_name=models.ForeignKey(User,models.CASCADE,limit_choices_to={'is_staff':True},related_name="staff",to_field='username')
    start_date=models.DateField()
    end_date=models.DateField()
    

    def __str__(self):
        return self.student_name.username
    
    
    
class ProjectAssign(models.Model):
    staff_name = models.ForeignKey(User,models.CASCADE,limit_choices_to={'is_staff':True},to_field='username')
    project_name = models.CharField(max_length=100,null=True,blank=True)
    startdate = models.DateField(max_length=100,null=True,blank=True)
    enddate = models.DateField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return self.staff_name.username
    
    
class DigitalTable(models.Model):
    client_name = models.CharField(max_length=100,null=True,blank=True)
    customer_id = models.CharField(max_length=50,null=True,blank=True)
    post = models.CharField(max_length=100,null=True,blank=True)
    Firm_name = models.CharField(max_length=100,null=True,blank=True)
    start_date = models.DateField(max_length=100,null=True,blank=True)
    end_date = models.DateField(max_length=100,null=True,blank=True)
    location = models.CharField(max_length=100,null=True,blank=True)
    amount_spend = models.CharField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return self.client_name
    
    
    
    
    
class TeamTable(models.Model):
    employee_name = models.ForeignKey(User,models.CASCADE,limit_choices_to={'is_staff':True},to_field='username')
    
    def __str__(self):
        return self.employee_name.username
    


class Leave(models.Model):
    STATUS_CHOICES = [
        ('pending','pending'),
        ('Approve','Approve'),
        ('Reject','Reject'),
        
   ]
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    duration_days = models.IntegerField()
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='pending')
    
    def save(self,*args,**kwargs):
        self.duration_days = (self.end_date - self.start_date).days + 1
        super().save(*args,**kwargs)
    def _str_(self):
        return f'Leave from{self.start_date} to {self.end_date}'
    
    

    
    

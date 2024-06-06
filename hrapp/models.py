from django.db import models
from authapp.models import User
# Create your models here.


class TeamleadAssign(models.Model):
    user = models.ForeignKey(User,models.CASCADE)
    tasktitle = models.CharField(max_length=100)
    startdate = models.DateField(max_length=100,null=True,blank=True)
    enddate = models.DateField(max_length=100,null=True,blank=True)
    task_description = models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.user.username
    
    
    


class StudentAssign(models.Model):
    student_name=models.ForeignKey(User,models.CASCADE,limit_choices_to={'is_intern':True})
    task_name=models.CharField(max_length=100,null=True,blank=True)
    task_details=models.CharField(max_length=100,null=True,blank=True)
    guide_name=models.CharField(max_length=100,null=True,blank=True)
    start_date=models.DateField()
    end_date=models.DateField()
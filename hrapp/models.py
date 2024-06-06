from django.db import models
from authapp.models import User
# Create your models here.


class TeamleadAssign(models.Model):
    user = models.ForeignKey(User,models.CASCADE, limit_choices_to={'is_teamlead':True})
    tasktitle = models.CharField(max_length=100)
    startdate = models.DateField(max_length=100,null=True,blank=True)
    enddate = models.DateField(max_length=100,null=True,blank=True)
    task_description = models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.user.username

# class ProjectAssign(models.Model):
#     team=models.ForeignKey(TeamleadAssign,models.CASCADE)
#     projectname=models.CharField(max_length=100)
#     employeename=models.CharField(max_length=100)
#     projectdate=models.DateField(max_length=100,null=True,blank=True)
#     deadline=models.DateField(max_length=100,null=True,blank=True)



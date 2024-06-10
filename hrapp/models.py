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
    
    
    


class StudentAssign(models.Model):
    student_name=models.ForeignKey(User,models.CASCADE,limit_choices_to={'is_intern':True},to_field='username')
    task_name=models.CharField(max_length=100,null=True,blank=True)
    task_details=models.CharField(max_length=100,null=True,blank=True)
    guide_name=models.ForeignKey(User,models.CASCADE,limit_choices_to={'is_staff':True},related_name="staff",to_field='username')
    start_date=models.DateField()   
    end_date=models.DateField()
    def __str__(self):
        return self.student_name.username
    

class AssignProject(models.Model):
    projectname=models.CharField(max_length=100,blank=True)
    employeename=models.ForeignKey(User,models.CASCADE,limit_choices_to={'is_staff':True},to_field='username')
    projectdate=models.DateField()
    deadline=models.DateField()
    def __str__(self):
        return self.projectname


# class LeaveRequest(models.Model):
#     PENDING = 'pending'
#     ACCEPTED = 'accepted'
#     REJECTED = 'rejected'

#     STATUS_CHOICES = [
#         (PENDING, 'Pending'),
#         (ACCEPTED, 'Accepted'),
#         (REJECTED, 'Rejected'),
#     ]
#     user=models.ForeignKey()
#     employee_id = models.IntegerField()
#     status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)

#     def __str__(self):
#         return f'LeaveRequest {self.id} - {self.status}'
    


class Leave(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    duration_days = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')

    def save(self, *args, **kwargs):
        self.duration_days = (self.end_date - self.start_date).days + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Leave from {self.start_date} to {self.end_date}'

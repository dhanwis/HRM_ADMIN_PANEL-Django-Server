from django.db import models
from authapp.models import User
import datetime
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
    time_slot=models.TimeField(default=datetime.time(0, 0))
    student_name=models.ForeignKey(User,models.CASCADE,limit_choices_to={'is_intern':True},to_field='username')
    task_name=models.CharField(max_length=100,null=True,blank=True)
    task_details=models.CharField(max_length=100,null=True,blank=True)
    guide_name=models.ForeignKey(User,models.CASCADE,limit_choices_to={'is_staff':True},related_name="staff",to_field='username')
    start_date=models.DateField()   
    end_date=models.DateField()
    def __str__(self):
        return self.student_name.username


class AssignProject(models.Model):
    projectname=models.CharField(max_length=100,blank=True,unique=True,null=True)
    employeename=models.ForeignKey(User,models.CASCADE,limit_choices_to={'is_staff':True},to_field='username')
    projectdate=models.DateField()
    deadline=models.DateField()
    def __str__(self):
        return self.projectname


class Leave(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]
    name= models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    duration_days = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')

    def save(self, *args, **kwargs):
        self.duration_days = (self.end_date - self.start_date).days + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Leave from {self.name.username}'


# class LeaveRequestConformation(models.Model):
#     STATUS_CHOICES = [
#         ('Pending', 'Pending'),
#         ('Approved', 'Approved'),
#         ('Rejected', 'Rejected'),
#     ]

#     candidate= models.ForeignKey(User, on_delete=models.CASCADE, related_name='username')
#     start_date = models.DateField()
#     end_date = models.DateField()
#     description = models.TextField()
#     duration_days = models.IntegerField(editable=False)
#     status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')

#     def save(self, *args, **kwargs):
#         self.duration_days = (self.end_date - self.start_date).days + 1
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return f'Leave from {self.start_date} to {self.end_date} ({self.status})'


{
        "id": 3,
        "start_date": "2024-06-08",
        "end_date": "2024-06-12",
        "description": "mbgg",
        "duration_days": 5,
        "status": "Pending"
    
}

class StatusShare(models.Model):
    projct_name = models.ForeignKey(AssignProject, models.CASCADE, to_field='projectname', related_name='status_shares')
    Teamleadname = models.ForeignKey(User, models.CASCADE, limit_choices_to={'is_teamlead': True})
    description = models.CharField(max_length=100, null=True, blank=True)
    note_upload = models.FileField(upload_to='uploads/')

    def _str_(self):
        return self.Teamleadname.username


class Noteupload(models.Model):
    note_upload= models.FileField(upload_to='uploads/')
    title=models.CharField(max_length=100,null=True,blank=True)
    description=models.CharField(max_length=100,null=True,blank=True)
    student_name=models.ForeignKey(User,models.CASCADE,limit_choices_to={'is_intern':True},to_field='username')

    def str(self):

        return self.student_name.username
    

class DigitalTable(models.Model):
    client_name = models.CharField(max_length=100,null=True,blank=True)
    customer_id = models.CharField(max_length=50,null=True,blank=True)
    post = models.CharField(max_length=100,null=True,blank=True)
    Firm_name = models.CharField(max_length=100,null=True,blank=True)
    start_date = models.DateField(max_length=100,null=True,blank=True)
    end_date = models.DateField(max_length=100,null=True,blank=True)
    location = models.CharField(max_length=100,null=True,blank=True)
    amount_spend = models.CharField(max_length=100,null=True,blank=True)
    
    def _str_(self):
        return self.client_name
    

class JobApply(models.Model):
    STATUS_CHOICES = [
        ('work from home','work from home'),
          ('work from office','work from office'),    
   ]
    EXPERIENCE_CHOICES = [
        ('0 year','0 year'),
        ('1 year','1 year'),
        ('2 years','2 years'),    
        ('more than 2 years','more than 2 years'),       
   ]
    company_name = models.CharField(max_length=100,null=True,blank=True)
    job_title=  models.CharField(max_length=100,null=True,blank=True)
    salary = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    mode_of_work  =models.CharField(max_length=100,choices=STATUS_CHOICES,default='work from office',null=True,blank=True)
    location = models.CharField(max_length=100,null=True,blank=True)
    experience  = models.CharField(max_length=100,choices=EXPERIENCE_CHOICES,null=True,blank=True)
    last_date  = models.DateField(null=True,blank=True)
    def str(self):
        return self.job_title
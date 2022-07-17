from django.db import models
from django.contrib.auth.models import User
from datetime import datetime



class UserTask(models.Model):
    status_choices = (('pending', 'pending'),
        ('completed', 'cmpleted'))
  
    task_name = models.CharField(max_length=200)
    task_description = models.TextField()
    assign_to=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(default=datetime.now)
    status=models.CharField(max_length = 100, choices = status_choices, default="pending")
    action=models.CharField(max_length=200)
    department = models.ForeignKey("Department",on_delete=models.CASCADE)
    def __str__(self):
      return self.task_name


class Department(models.Model):
    Department_name = models.CharField(max_length = 100)
    def __str__(self):
      return self.Department_name



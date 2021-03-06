from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User



class Project(models.Model):
    project_name = models.CharField(max_length=200)
    userp = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.project_name



class Task(models.Model):
    usert = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    task = models.CharField(max_length=300)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=datetime.now())
    end_time = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.task

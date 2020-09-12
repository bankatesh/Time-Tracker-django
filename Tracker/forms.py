from django import forms
from django.forms import ModelForm
import datetime
from .models import *


class TaskForm(forms.ModelForm):
    taskform = forms.CharField(max_length=300)
    #projectform = forms.ForeignKey(Project, on_delete=models.CASCADE)
    start_timeform= forms.DateTimeField(initial=datetime.now())
    end_timeform = forms.DateTimeField(initial=datetime.now())
    class Meta:
        model = Task
        fields = ['project']

    '''
    class Meta:
        model = Task
        fields = '__all__'
    '''


class ProjectForm(forms.Form):
    project_nameform = forms.CharField(max_length=200)
    '''
    class Meta:
        model = Project
        fields = ['project_name']

    '''

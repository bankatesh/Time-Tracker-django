from django import forms
from django.forms import ModelForm
from .models import *


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name']


from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from Tracker.models import *
from Tracker.forms import *



@login_required(login_url='/accounts/login')
def add(request):
    TaskF = TaskForm()
    ProjectF = ProjectForm()
    context = {
        'taskf': TaskF,
        'projectf': ProjectF,
    }
    log_user = request.user
    if request.method == 'POST':
        if 'projectf' in request.POST:
            ProjectF = ProjectForm(request.POST )

            if ProjectF.is_valid():
                ProjectF.save()

            return redirect(add)

        elif 'taskf' in request.POST:
            TaskF = TaskForm(request.POST)
            if TaskF.is_valid():
                TaskF.save()
            return redirect(dash)

    return render(request,'add.html',context)

@login_required(login_url='/accounts/login')
def dash(request):
    log_user = request.user
    TaskM = Task.objects.all()
    ProjectM = Project.objects.all()
    context1 = {
        'taskm': TaskM,
        'projectm': ProjectM,
    }
    return render(request,'dashboard.html',context1)


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

            data = request.POST['project_nameform']
            new = Project(project_name=data, userp =log_user)
            #ProjectF = ProjectForm(request.POST )
            new.save()

            #if ProjectF.is_valid():
             #   ProjectF.save()

            return redirect(add)

        elif 'taskf' in request.POST:

            data1 = request.POST
            pk = data1['project']
            new2 = Task(task=data1['taskform'],project = Project.objects.get(id=pk),start_time=data1['start_timeform'],end_time = data1['end_timeform'], usert = log_user)
            new2.save()
            return redirect(dash)

            '''
            if TaskF.is_valid():
                TaskF.save()
            return redirect(dash)
            '''


    return render(request,'add.html',context)

@login_required(login_url='/accounts/login')
def dash(request):
    log_user = request.user
    TaskM = Task.objects.filter(usert = log_user)
    ProjectM = Project.objects.filter(userp=log_user)
    context1 = {
        'taskm': TaskM,
        'projectm': ProjectM,
    }
    return render(request,'dashboard.html',context1)


from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

'''
# Create your views here.
@login_required(login_url='/accounts/login')
def show(request):
    log_user = request.user
    memories = memory.objects.filter(user=log_user)
    return render(request, 'showdiary.html', {'m':memories})

@login_required(login_url='/accounts/login')
def add(request):
    if request.method == "POST":
        data = request.POST['data']
        new = memory(content=data, user=request.user)
        new.save()
        return render(request, 'addmemory.html')
    else:
        return render(request, 'addmemory.html')
'''

def dash(request):
    return render(request,'dashboard.html')

def add(request):
    TaskF = TaskForm()
    ProjectF = ProjectForm()
    context = {
        'taskf': TaskF,
        'projectf': ProjectF,
    }

    if request.method == 'POST':
        if 'projectf' in request.POST:
            ProjectF = ProjectForm(request.POST)
            if ProjectF.is_valid():
                ProjectF.save()
            return redirect(add)

        elif 'taskf' in request.POST:
            TaskF = TaskForm(request.POST)
            if TaskF.is_valid():
                TaskF.save()
            return redirect(dash)

    return render(request,'add.html',context)

def dashboard(request):
    TaskM = Task.objects.all()
    ProjectM = Project.objects.all()
    context1 = {
        'taskm': TaskM,
        'projectm': ProjectM,
    }
    return render(request,'dashboard.html',context1)


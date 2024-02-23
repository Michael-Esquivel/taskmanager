from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.utils import timezone
from .forms import taskF
from .models import taskM
from django.contrib.auth.decorators import login_required

def home(request):
     return render(request, 'base.html', {'INICIO': 'INICIO'})  

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'form' : UserCreationForm})
    else:
        try: 
            if request.POST['password1'] == request.POST['password2']: 
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'] ) #create_user
                login(request, user)
            else:
                 return render(request, 'signup.html', {'form' : UserCreationForm, 'error': 'Passwords are wrong'})
        except IntegrityError:
                return render(request, 'signup.html', {'form' : UserCreationForm, 'error': 'User already exist'})
        
        return redirect('tasks')
    
@login_required
def createTask(request):
     if request.method == 'GET':
        return render(request, 'createTask.html', {'form':taskF})
     else: 
          form = taskF(request.POST)            #Se envian datos al objeto taskM
          new_task = form.save(commit=False)    #Devuelve el objeto taskM
          new_task.user = request.user
          new_task.save()
          return redirect('tasks')

@login_required
def Logout(request):
    logout(request) 
    return redirect('home')

def Login(request):
     if request.method == 'GET':
          return render(request, 'login.html', {'form':AuthenticationForm})
     else: 
          user = authenticate(request, 
                              username = request.POST['username'], password = request.POST['password']) #Si un dato esta mal, devuelve None
          if user:  
               login(request, user)
               return redirect('tasks')
          return render(request, 'login.html', {'form':AuthenticationForm, 'error':'Username or password is incorrect'})
     
@login_required
def tasks(request):
     task = taskM.objects.filter(user = request.user, dateComplete__isnull= True)
     return render(request, 'tasks.html', {'tasks' : task})

@login_required
def editTask(request, id):
     if request.method == 'GET':
          task = get_object_or_404(taskM, pk=id, user = request.user) #El usuario solo accede a sus tareas
          form = taskF(instance = task)
          return render(request, 'editTask.html', {'form':form, 'task':task})
     else: 
          task = get_object_or_404(taskM, pk=id, user = request.user)
          form = taskF(request.POST, instance = task)  #Recoge datos del form y lo faltante lo llena del task
          form.save()
          return redirect('tasks')

@login_required
def deleteTask(request, id):
     task = get_object_or_404(taskM, pk=id, user = request.user)
     if request.method == 'POST':
          task.delete()
          return redirect('tasks')
     

@login_required
def completeTask(request, id):
     task = get_object_or_404(taskM, pk=id, user = request.user)
     if request.method == 'POST':
          task.dateComplete = timezone.now()
          task.save()
          return redirect('tasks')

@login_required
def tasksComplete(request):
     task = taskM.objects.filter(user = request.user, dateComplete__isnull = False).order_by('-dateComplete')
     return render(request, 'tasks.html', {'tasks':task})
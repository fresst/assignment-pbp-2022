import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from todolist.models import Task, CreateTaskForm

# Create your views here.
# authentication
def user_register(req):
    form = UserCreationForm()
    
    if req.method == "POST":
        form = UserCreationForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req, 'Akun berhasil dibuat!')
            return redirect('todolist:user_login')
    context = {'form' : form}
    return render(req, 'register.html', context)

def user_login(req):
    if req.method == 'POST':
        user_name = req.POST.get('username')
        user_pass = req.POST.get('password')
        user = authenticate(req, username=user_name, password=user_pass)
        if user is not None:
            login(req, user)
            response = HttpResponseRedirect(reverse('todolist:show_todolist'))
            response.set_cookie('login_cookie', str(datetime.datetime.now()))
            return response
        else:
            messages.info(req, 'username atau password salah!')
    context = {}
    return render(req, 'login.html', context)

def user_logout(req):
    logout(req)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('login_cookie')
    return response

# todolist
@login_required(login_url='/todolist/login')
def show_todolist(req):
    user_name = req.user.username
    task = Task.objects.filter(user=req.user)
    
    context = {
        'name' : user_name,
        'tasks' : task,
        'last_login' : req.COOKIES['login_cookie']
    }
    return render(req, 'todolist.html', context)

@login_required(login_url='/todolist/login')
def create_task(req):
    form = CreateTaskForm()
    if req.method == 'POST':
        form = CreateTaskForm(req.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.user = req.user
            new_task.date = f"{datetime.datetime.now():%Y-%m-%d}"
            new_task.save()
            # messages.success(req, 'Task baru berhasil dibuat!')
            return redirect('todolist:show_todolist')
    context = {'form' : form}
    return render(req, 'create-task.html', context)
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username= username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login succesfull!')
            return redirect('tareas:home')
    return render(request,'registration/login.html')


def logout_usuario(request):
    messages.success(request,'LOGOUT SUCCESFULL')
    logout(request)
    
    return redirect('usuarios:login')




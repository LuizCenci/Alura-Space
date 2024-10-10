from django.shortcuts import render, redirect
from apps.users.forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth, messages

def login(request):
    username = request.user.username
    form = login_form()
    if request.method == 'POST':
        form = login_form(request.POST)
        if form.is_valid():
            name = form['login_name'].value()
            password = form['password'].value()
            user = authenticate(request, username = name, password = password)

            if user is None:
                messages.error(request, 'Usuário ou senha incorreta!')
                return redirect('login')
            
            auth.login(request, user)
            return redirect('index')
            
    context = {'username':username, 'form':form}        

    return render(request, "users/login.html", context)

def register(request):
    username = request.user.username
    form = singup_form()
    if request.method == 'POST':
        form = singup_form(request.POST)
        if form.is_valid():
            
            first_name = form['first_name'].value()
            surname = form['surname'].value()
            name = form['register_name'].value()
            email = form['email'].value()
            password = form['password'].value()

            if User.objects.filter(username=name).exists():
                messages.error(request, 'Nome já utilizado!')
                return redirect('register')
            
            user = User.objects.create_user(
                first_name=first_name,
                last_name=surname,
                username=name,
                email=email,
                password=password
            )
            user.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('login')
    
    context = {'username':username, 'form':form}
    return render(request, "users/register.html", context)

def logout(request):
    username = request.user.username
    auth.logout(request)
    messages.success(request, f'{username} Desconectou-se!')
    return redirect('login')
from django.shortcuts import render
from users.forms import *

def login(request):
    form = login_form()
    return render(request, "users/login.html", {'form':form})

def cadastro(request):
    form = singup_form()
    
    return render(request, "users/cadastro.html", {'form':form})
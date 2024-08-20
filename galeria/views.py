from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, 'galeria/index.html')

def image(request):
    return render(request, 'galeria/imagem.html')
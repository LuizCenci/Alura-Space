from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from galeria.models import *
# Create your views here.

def index(request): 
    if not request.user.is_authenticated:
        messages.error(request, 'Por favor, realize seu login para acessar o site')
        return redirect('login')
    
    username = request.user.username
    photos = photo.objects.order_by('-publish_date').filter(published = True)
    context = {'username':username, 'cards':photos}
    return render(request, 'galeria/index.html', context)

def image(request, item_id):
    username = request.user.username
    image = get_object_or_404(photo, pk=item_id)
    context = {'username':username, 'image':image}
    return render(request, 'galeria/imagem.html', context)

def search(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Por favor, realize seu login para acessar o site')
        return redirect('login')
    
    username = request.user.username
    photos = photo.objects.order_by('-publish_date').filter(published = True)
    search_text = ''
    if 'search_text' in request.GET:
        search_text = request.GET['search_text']
        if search_text:
            photos = (photos.filter(name__icontains=search_text) | photos.filter(description__icontains=search_text)
                      | photos.filter(tag__icontains=search_text))


    context = {
        'username':username,
        'cards':photos,
        'search_text':search_text
    }
    return render(request, 'galeria/search.html', context)
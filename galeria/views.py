from django.shortcuts import render, get_object_or_404
from galeria.models import *
# Create your views here.

def index(request):
    photos = photo.objects.order_by('-publish_date').filter(published = True)
    return render(request, 'galeria/index.html', {'cards':photos})

def image(request, item_id):
    image = get_object_or_404(photo, pk=item_id)
    return render(request, 'galeria/imagem.html', {"image":image})

def search(request):
    photos = photo.objects.order_by('-publish_date').filter(published = True)
    search_text = ''
    if 'search_text' in request.GET:
        search_text = request.GET['search_text']
        if search_text:
            photos = (photos.filter(name__icontains=search_text) | photos.filter(description__icontains=search_text)
                      | photos.filter(tag__icontains=search_text))


    context = {
        'cards':photos,
        'search_text':search_text
    }
    return render(request, 'galeria/search.html', context)
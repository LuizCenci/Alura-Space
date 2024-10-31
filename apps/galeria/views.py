from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from apps.galeria.models import *
from apps.galeria.forms import *
# Create your views here.

def index(request): 
    if not request.user.is_authenticated:
        messages.error(request, 'Por favor, realize seu login para acessar o site')
        return redirect('login')
    
    username = request.user.username
    photos = photo.objects.order_by('name').filter(published = True)
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
            photos = (photos.filter(name__icontains=search_text) 
                      | photos.filter(tag__icontains=search_text))


    context = {
        'username':username,
        'cards':photos,
        'search_text':search_text
    }
    return render(request, 'galeria/index.html', context)

def newest(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Por favor, realize seu login para acessar o site')
        return redirect('login')
    
    username = request.user.username
    photos = photo.objects.order_by('-publish_date').filter(published = True)

    context = {
        'username':username,
        'cards':photos,
    }
    
    return render(request, 'galeria/index.html', context)
def new_image(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Por favor, realize seu login para acessar o site')
        return redirect('login')
    
    username = request.user.username

    form = photo_form(initial={'user':request.user.username})
    if request.method == 'POST':
        form = photo_form(request.POST, request.FILES)
        if form.is_valid():
            new_image_instance = form.save(commit=False)
            new_image_instance.user = request.user
            new_image_instance = form.save()
            messages.success(request, 'Nova imagem salva')
            return redirect('index')
    context = {'form':form, 'username':username}
    return render(request, 'galeria/new_image.html', context)


def edit_image(request, item_id):
    username = request.user.username
    infos = photo.objects.get(id=item_id)
    form = photo_form(instance=infos)

    if request.method == 'POST':
        form = photo_form(request.POST, request.FILES, instance=infos)
        if form.is_valid():
            form.save()
            messages.success(request, 'Imagem salva')
            return redirect('index')
    context = {'form':form, 'username':username, 'item_id':item_id}
    return render(request, 'galeria/edit_image.html', context)

def delete_image(request, item_id):
   
    infos = photo.objects.get(id=item_id)
    infos.delete()
    messages.success(request, 'Imagem removida')
    return redirect('index')

def filter(request, tag):
    username = request.user.username
    photos = photo.objects.order_by('-publish_date').filter(published = True, tag = tag)
    context = {
        'username':username,
        'cards':photos,
        'tag':tag
    }
    return render(request, 'galeria/index.html', context)
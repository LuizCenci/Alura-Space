from django.urls import path
from galeria.views import *

urlpatterns = [
    path('', index, name='index'),    
    path('imagem/<int:item_id>', image, name='image'),
    path('search', search, name='search')
]
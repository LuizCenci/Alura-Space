from django.urls import path
from apps.galeria.views import *

urlpatterns = [
    path('', index, name='index'),    
    path('imagem/<int:item_id>', image, name='image'),
    path('search', search, name='search'),
    path('new-image', new_image, name='new_image'),
    path('edit-image/<int:item_id>', edit_image, name='edit_image'),
    path('delete-image/<int:item_id>', delete_image, name='delete_image'),
    path('filter/<str:tag>', filter, name='filter'),
    path('novas', newest, name='newest')
]
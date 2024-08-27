from django.contrib import admin
from galeria.models import *

# Register your models here
class PhotosList(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id','name')
    search_fields = ('name',)
    list_filter = ('tag',)
admin.site.register(photo, PhotosList)
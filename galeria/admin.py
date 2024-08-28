from django.contrib import admin
from galeria.models import *

# Register your models here
class PhotosList(admin.ModelAdmin):
    list_display = ('id', 'name', 'published')
    list_display_links = ('id','name')
    search_fields = ('name',)
    list_filter = ('tag',)
    list_per_page = 10
    list_editable = ('published',)
admin.site.register(photo, PhotosList)
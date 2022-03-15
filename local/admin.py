from django.contrib import admin
from .models import Local

class ListandoLocais(admin.ModelAdmin):
    list_display = ('tipo', 'titulo', 'numero', 'endereco',)
    list_display_links = ('tipo', 'titulo')
    search_fields = ('tipo',)
    list_filter = ('tipo',)
    list_per_page = 10
 
admin.site.register(Local, ListandoLocais)

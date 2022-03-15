from django.contrib import admin
from .models import Endereco
 
class ListandoEndereco(admin.ModelAdmin):
    list_display = ('logradouro', 'bairro', 'cidade', 'cep', 'uf',)
    list_display_links = ('logradouro', 'bairro')
    search_fields = ('logradouro',)
    list_filter = ('logradouro',)
    list_per_page = 10
 
admin.site.register(Endereco, ListandoEndereco)
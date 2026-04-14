from django.contrib import admin
from .models import Empresa, Patente

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('cnpj', 'razao_social')
    search_fields = ('cnpj', 'razao_social')
 
@admin.register(Patente)
class PatenteAdmin(admin.ModelAdmin):
    list_display = ('numero_registro', 'titulo', 'empresa')
    search_fields = ('numero_registro', 'titulo', 'empresa__cnpj', 'empresa__razao_social')


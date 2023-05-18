from django.contrib import admin
from .models import Estrutura


class EstruturaAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'titulo', 'sigla', 'nivel', 'acervo', 'estrutura_nivel_superior')
    list_display_links = ('id', 'codigo', 'titulo', 'sigla', 'nivel', 'acervo', 'estrutura_nivel_superior')
    search_fields = ('titulo', 'descricao', 'info_adicionais')
    list_filter = ('estrutura_nivel_superior', 'acervo')

admin.site.register(Estrutura, EstruturaAdmin)


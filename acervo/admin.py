from django.contrib import admin
from acervo.models import Acervo


class AcervoAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'titulo', 'sigla', 'ordem_exibicao')
    list_display_links = ('id', 'codigo', 'titulo', 'sigla', 'ordem_exibicao')
    search_fields = ('titulo', 'descricao', 'info_adicionais')

admin.site.register(Acervo, AcervoAdmin)

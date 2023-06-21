from django.contrib import admin
from pessoa.models import Pessoa


class PessoaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)

admin.site.register(Pessoa, PessoaAdmin)

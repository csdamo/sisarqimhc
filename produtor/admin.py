from django.contrib import admin
from produtor.models import Produtor


class ProdutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'titulo')
    list_display_links = ('id', 'codigo', 'titulo')
    search_fields = ('titulo', 'codigo')

admin.site.register(Produtor, ProdutorAdmin)

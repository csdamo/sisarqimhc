from django.contrib import admin
from assunto.models import Assunto


class AssuntoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo')
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo',)

admin.site.register(Assunto, AssuntoAdmin)


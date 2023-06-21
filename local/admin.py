from django.contrib import admin
from local.models import Local


class LocalAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo')
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo',)

admin.site.register(Local, LocalAdmin)

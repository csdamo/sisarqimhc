from django.contrib import admin

from objetodigital.models import ObjetoDigital



class ObjetoDigitalAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'documento', 'qualidade' )
    list_display_links = ('id', 'codigo', 'documento', 'qualidade')

admin.site.register(ObjetoDigital, ObjetoDigitalAdmin)


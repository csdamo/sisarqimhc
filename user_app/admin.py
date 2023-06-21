from django.contrib import admin
from .models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email')
    list_display_links = ('id', 'username', 'email')
    search_fields = ('username', 'email')

admin.site.register(Account, AccountAdmin)


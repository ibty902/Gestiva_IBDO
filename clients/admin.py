from django.contrib import admin
from .models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'email', 'telephone', 'ville')
    search_fields = ('nom', 'email', 'ville')

# Register your models here.

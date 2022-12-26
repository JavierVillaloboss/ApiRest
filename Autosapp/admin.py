from django.contrib import admin
from Autosapp.models import Autos,Tienda,Repuesto
# Register your models here.

class Autosadmin(admin.ModelAdmin):
    list_display = ['marca','modelo','año','transmicion','kilometraje','estado']

admin.site.register(Autos,Autosadmin)

class Tiendaadmin(admin.ModelAdmin):
    list_display = ['direccion','nombre','tel','horario','correo','calidad']

admin.site.register(Tienda,Tiendaadmin)

class Repuestoadmin(admin.ModelAdmin):
    list_display = ['motores','neumaticos','llantas','aceites','baterias','suspensiones']

admin.site.register(Repuesto,Repuestoadmin)
from django.contrib import admin
from apiRest.models import Autos,Tienda,Repuesto
# Register your models here.

class Autosadmin(admin.ModelAdmin):
    list_display = ['marca','modelo','año','transmicion','kilometraje','estado']

class Tiendaadmin(admin.ModelAdmin):
    list_display=['direccion','nombre','tel','horario','correo','calidad']

class Repuestoadmin(admin.ModelAdmin):
    list_display = ['motores','neumaticos','llantas','aceites','baterias','suspensiones','autos','tiendas']
from django.contrib import admin
from django.urls import path
from Autosapp.views import RegistroView,RegistroRe,RegistroTi
from Autosapp import views
from apiRest import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('autos',views.autos_list),
    path('autos/<int:pk>',views.autos_detail),
    path('tiendas',views.tienda_list),
    path('tiendas/<int:pk>',views.tienda_detail),
    path('repuestos',views.repuesto_list),
    path('repuestos/<int:pk>',views.repuesto_detail),
]
 
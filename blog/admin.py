from django.contrib import admin
from .models import Vehiculo, Categoria, FotoVehiculo, Favorito


# Permite agregar varias fotos dentro del vehículo
class FotoVehiculoInline(admin.TabularInline):
    model = FotoVehiculo
    extra = 3


# Panel de administración de vehículos
@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    inlines = [FotoVehiculoInline]


# Registrar los demás modelos
admin.site.register(Categoria)
admin.site.register(Favorito)
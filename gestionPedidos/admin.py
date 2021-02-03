from django.contrib import admin

from gestionPedidos.models import Clientes, Articulos, Pedidos

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display=("nombre", "direccion", "tfno")
    search_fields=("nombre", "tfno")


class ArtticulosAdmin(admin.ModelAdmin):
    list_filter=("seccion",)


class PedidosAdmin(admin.ModelAdmin):
    list_display=("numero", "fecha")
    list_filter=("fecha",)
    date_hierarchy="fecha"


admin.site.register(Clientes, ClienteAdmin)
admin.site.register(Articulos, ArtticulosAdmin)
admin.site.register(Pedidos, PedidosAdmin)

from django.urls import path
from .views import * #Pongo el * para que me traiga todos los metodos

urlpatterns = [
    path('', list_products, name='listado_productos'), 
    path('crear/', create_product, name='crear_producto'),
    path('editar/<id>', edit_product, name='editar_producto'),
    path('actualizar/<id>', update_product, name='actualizar_producto'),
    path('eliminar/<id>', delete_product, name='eliminar_producto'),
]
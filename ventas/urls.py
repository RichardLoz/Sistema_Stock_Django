from django.urls import path
from .views import * #Pongo el * para que me traiga todos los metodos

urlpatterns = [
    path('', list_invoices, name='listado_facturas'), 
]
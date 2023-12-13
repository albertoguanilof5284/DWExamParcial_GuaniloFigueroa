from django.urls import path
from .import views

app_name = 'gestionTienda'

urlpatterns = [
    path('',views.index,name='index'),
    path('productos',views.productos,name='productos'),
    path('tiendas',views.tiendas,name='tiendas'),

    path('agregarTienda',views.agregarTienda,name='agregarTienda'),
    path('agregarProducto',views.agregarProducto,name='agregarProducto'),

    path('editarProducto/<str:idProducto>',views.editarProducto,name='editarProducto'),
    path('saveProducto',views.saveProducto,name='saveProducto'),

    path('eliminarProducto/<str:idProducto>',views.eliminarProducto,name='eliminarProducto'),
    path('eliminarTienda/<str:idTienda>',views.eliminarTienda,name='eliminarTienda'),

    path('detalleTienda/<str:idTienda>',views.detalleTienda,name='detalleTienda')
]
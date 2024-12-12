from django.urls import path

from inventario import views
urlpatterns = [
    path('', views.home),
    path('registrarProducto/', views.registrarProducto),
    path('eliminarProducto/<int:id>/', views.eliminarProducto),
    path('editarProducto/<int:id>/', views.editarProducto),
    path('adicionarProducto/', views.adicionarProducto),    
]
from rest_framework import serializers
from inventario.models import Producto
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'  # ['id', 'nombre', 'descripcion', 'marca', 'cantidad_min', 'cantidad_max', 'precio']
        
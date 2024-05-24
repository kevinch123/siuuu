from rest_framework import serializers
from .models import Pedidos

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pedidos
        #fields=('id','titulo','descripcion','done')
        fields='__all__'
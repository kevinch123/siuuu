from django.shortcuts import render
from rest_framework import viewsets
from .serializer import PedidoSerializer
from .models import Pedidos

# Create your views here.

class PedidoView(viewsets.ModelViewSet):
    serializer_class= PedidoSerializer
    queryset=Pedidos.objects.all()

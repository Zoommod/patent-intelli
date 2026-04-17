from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Empresa, Patente
from .serializers import EmpresaSerializer, PatenteSerializer

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class PatenteViewSet(viewsets.ModelViewSet):
    queryset = Patente.objects.all()
    serializer_class = PatenteSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['titulo']
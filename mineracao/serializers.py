from rest_framework import serializers
from .models import Empresa, Patente

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'

class PatenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patente
        fields = '__all__'
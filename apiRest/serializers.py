from rest_framework import serializers
from apiRest.models import Tienda,Autos,Repuesto

class autosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autos
        fields = '__all__'

class tiendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tienda
        fields = '__all__'

class repuestoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repuesto
        fields = '__all__'
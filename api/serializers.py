from rest_framework import serializers
from .models import Eco, Country

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class EcoSerializer(serializers.ModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = Eco
        fields = '__all__'
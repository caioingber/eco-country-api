from rest_framework import serializers
from models import Eco, Country

class CountrySerializer(serializers.modelSerializer):
    class Meta:
        Model = Country
        fields = '__all__'

class EcoSerializer(serializers.modelSerializer):
    country = CountrySerializer()

    class Meta:
        Model = Eco
        fields = '__all__'
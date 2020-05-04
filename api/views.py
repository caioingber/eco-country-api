from django.shortcuts import render
from .models import Eco, Country
from .serializers import EcoSerializer, CountrySerializer
from rest_framework import generics

class CountryList(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer



class EcoList(generics.ListAPIView):
    serializer_class = EcoSerializer
    
    def get_queryset(self):
        queryset = Eco.objects.all()
        region = self.request.query_params.get('region', None)
        if region is not None:
            queryset = queryset.filter(region=region)
        return queryset


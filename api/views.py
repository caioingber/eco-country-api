from django.shortcuts import render
from models import Eco, Country
from serializers import EcoSerializer, CountrySerializer
from rest_framework import generics

class CountryList(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer



class EcoList(generics.ListAPIView):
    queryset = Eco.objects.all()
    serializer_class = EcoSerializer


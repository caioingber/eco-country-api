from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=200)
    capital = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    subregion = models.CharField(max_length=200)
    population = models.FloatField(null=True, blank=True)
    area = models.FloatField(null=True, blank=True)
    gini = models.FloatField(null=True, blank=True)
    flag = models.URLField(max_length=200)

class Eco(models.Model):
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    region = models.CharField(max_length=200, null=True, blank=True)
    hdi = models.FloatField(null=True, blank=True)
    gdpPerCapita = models.CharField(max_length=50, null=True, blank=True)
    cropFootprint = models.FloatField(null=True, blank=True)
    forestFootprint = models.FloatField(null=True, blank=True)
    carbonFootprint = models.FloatField(null=True, blank=True)
    ecoFootprint = models.FloatField(null=True, blank=True)
    totalBiocapacity = models.FloatField(null=True, blank=True)
    biocapacityReserve = models.FloatField(null=True, blank=True)
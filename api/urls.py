from django.urls import path
from .views import CountryList, EcoList

urlpatterns = [
    path('countries', CountryList.as_view(), name='countries_list'),
    path('ecos', EcoList.as_view(), name='ecos_list'),
]
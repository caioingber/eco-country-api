import json
from requests import get

data = get("https://restcountries.eu/rest/v2/all")
data_json = data.json()

countries = []

for country in data_json:
    countries.append({
        "model": "api.country",
        "pk": data_json.index(country) + 1,
        "fields": {
            "name": country['name'],
            "capital": country['capital'],
            "region": country['region'],
            "subregion": country['subregion'],
            "population": country['population'],
            "area": country['area'],
            "gini": country['gini'],
            "flag": country['flag']
        }
    })


with open('api/fixtures/countries.json', 'w') as outfile:
    json.dump(countries, outfile)
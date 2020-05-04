import json

modified = []

countries = json.load(open('api/countries.json'))
ecos = json.load(open('api/ecofootprintdata.json'))
        

for country in countries:
    for eco in ecos:
        if country['fields']['name'] == eco['country']:
            modified.append({
                'model': "api.eco",
                "pk": ecos.index(eco) + 1,
                "fields": {
                    "country": country['pk'],
                    "region": country['fields']['region'],
                    "hdi": eco['hdi'],
                    "gdpPerCapita": eco['gdpPerCapita'],
                    "cropFootprint": eco["cropFootprint"],
                    "forestFootprint": eco["forestFootprint"],
                    "carbonFootprint": eco["carbonFootprint"],
                    "ecoFootprint": eco["ecoFootprint"],
                    "totalBiocapacity": eco["totalBiocapacity"],
                    "biocapacityReserve": eco["biocapacityReserve"]
                }
            })

with open('api/fixtures/ecofixtures.json', 'w') as outfile:
    json.dump(modified, outfile)





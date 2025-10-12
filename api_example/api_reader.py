import requests
from tqdm import tqdm
import pandas as pd

res = requests.get(
    url="https://api.gbif.org/v1/species/match/",
    params={"species": "Condylostomides terricola"},
)
print(res.json())
#чтение в цикле и исправление ошибок
species_list = [
    "Homo sapiens", "Canis lupus", "Felis catus", "Ursus arctos", "Panthera leo", 
    "Elephas maximus", "Delphinus delphis", "Aquila chrysaetos", "Rosa canina", 
    "Quercus robur", "Drosophila melanogaster", "Escherichia coli"
] * 10 
species_list = species_list[:100]

results = []

for species in tqdm(species_list):
    res = requests.get("https://api.gbif.org/v1/species/match/", params={"species": species})
    data = res.json()
    data['queried_species'] = species
    
    if res.status_code == 200:
        data['request_status'] = 'success'
    else:
        data['request_status'] = f'http_error_{res.status_code}'
    
    results.append(data)

df = pd.DataFrame(results)
print(f"Готово! Записей: {len(df)}")

print("\nСтатусы запросов:")
status_counts = df['request_status'].value_counts()
for status, count in status_counts.items():
    print(f"{status}: {count} записей") 
#приведение типов
df['confidence'] = pd.to_numeric(df['confidence'], errors='coerce')
df['matchType'] = df['matchType'].astype(str)
df['kingdom'] = df['kingdom'].astype(str)
df['phylum'] = df['phylum'].astype(str)
df['class'] = df['class'].astype(str)
df['order'] = df['order'].astype(str)
df['family'] = df['family'].astype(str)
df['genus'] = df['genus'].astype(str)
df['species'] = df['species'].astype(str)
df['status'] = df['status'].astype(str)
df['queried_species'] = df['queried_species'].astype(str)
df['request_status'] = df['request_status'].astype(str)
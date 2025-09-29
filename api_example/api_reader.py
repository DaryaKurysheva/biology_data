import requests
from tqdm import tqdm
import pandas as pd

res = requests.get(
    url="https://api.gbif.org/v1/species/match/",
    params={"genus": "Bombus"},
)
print(res.json())

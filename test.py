import pandas as pd
import json
import numpy as np

address = pd.read_csv('address_work.csv')
address_dict = dict()

for i in range(len(address)):
    name = address['address'][i]
    lat = address['latitude'][i]
    lon = address['longitude'][i]

    address_dict[name] = {"latitude": lat, "longitude": lon}

with open('address_dict.json', 'w', encoding = 'utf-8') as f:
    json.dump(address_dict, f, ensure_ascii = False, indent = 4)

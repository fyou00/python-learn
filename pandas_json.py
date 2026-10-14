import pandas as pd
import json

with open('https://www.themealdb.com/api/json/v1/1/filter.php?c=Chicken', 'r') as f:
    data = json.load(f)

df = pd.json_normalize(data)

print(df)
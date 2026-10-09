import requests
import pandas as pd

url = 'https://www.themealdb.com/api/json/v1/1/filter.php?c=Chicken'

response = requests.get(url)
data = response.json()

# for meal in data['meals'] :
#   print(meal['strMeal'])

df = pd.json_normalize(data['meals'])
df = df[['strMeal', 'idMeal', 'strArea', 'strCountry']]
print(df)
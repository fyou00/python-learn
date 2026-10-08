import requests
# import pandas as pd

url = 'https://www.themealdb.com/api/json/v1/1/filter.php?c=Beef'
response = requests.get(url)

if response.status_code == 200:
  data = response.json()
  # df = pd.DataFrame(data)
  # print()
  # print(df)
  for i in data['meals']:
    print(i['strMeal'])
else:
    print(f"gagal mengambil data. error code: {response.status_cowde}")
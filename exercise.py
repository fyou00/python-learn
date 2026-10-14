# list_aja = [i+5 if i % 2 == 0 else i+9 for i in range (10)]
# print(list_aja)

# python slicing data[start:stop:step]

# uppercase huruf pertama
# nama = ['apple', 'banana', 'orange']
# list_upper = [nama[0].upper() + nama[1:] for nama in nama]
# print(list_uppers\)asd

# print("mengambil data dari list menggunakan loop biasa")
# data = ['cpu', 'motherboard', 'ssd']
# for i in range(len(data)):
#   print(f"Index {i}: {data[i]}")
  
# print("=================\n")

# print("mengambil data dari list menggunakan enumerate")
# for i, data in enumerate(data):
#   print(f"Index {i}: {data}")

data = []

for i in range(10):
  if i % 2 == 0:
    data.append(i+1)
print(data)
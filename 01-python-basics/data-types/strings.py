# ini single quote, bisa \n buat enter kebawah
greeting = 'Hello,\nworld!'
print(greeting)

# double quote, sama aja cuma bedanya kita bisa tambahin '' didalamnya
greeting = "Hello, 'World!'"
print(greeting)

# triple quoted, bisa tambhin simbol kayak string didalam string itu sendiri
teks_panjang = """
nah disini kita bebas buat masukin berapa
baris teks yang kita mau, kita juga bisa 
buat add something like 'petik satu' atau
petik dua"
""" 
print(teks_panjang)

# raw strings
normal_string = "C:\nama\baru" # \n diproses
raw_string = r"C:\nama\baru" # simbol diabaikan, sehingga \n tidak diproses
print(normal_string)
print(raw_string)

# f-string
nama = "fathur" # variable tester
formatted_string = f"namaku {nama}" # isikan nama variable didalam {}
print(formatted_string)

# STRING ADALAH ARRAY
x = 'namaku rem'
print(x[-2]) # ngeprint array x pada index kedua terakhir yang berarti huruf e
#x[8] = 'a' # ngubah index ke-8 jadi huruf a, ga bisa karena string itu IMMUTABLE

nama = 'edogawa conan'.capitalize()
print(nama)
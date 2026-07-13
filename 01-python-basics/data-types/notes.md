# Data Types

> Materi: Python Basics → Data Types

---

# Integer

## Apa itu Integer?

Integer adalah bilangan bulat tanpa angka desimal.

Contoh:

```python
age = 20
temperature = -5
```

### Operasi

```python
10 + 5
10 - 5
10 * 5
10 / 5
10 // 3
10 % 3
10 ** 2
```

---

## String

String adalah kumpulan karakter yang diapit tanda petik. bersifat IMMUTABLE (gabisa diubah)

```python
name = "Fathur"
city = 'Lhokseumawe'
```

### Method string

Format penulisan string method adalah nama_variabel.nama_method(argumen).

String method normalnya ditulis begini
```python
nama = 'edogawa conan'
nama.capitalize()
```

atau bisa juga gini
```python
nama = 'edogawa conan'.capitalize()
```


---

# Penting

- Python bersifat dynamically typed.
- Gunakan `type()` untuk melihat tipe data.
- Gunakan `isinstance()` untuk mengecek tipe data.

```python
print(type(10))
print(type("Hello"))
print(type(True))
```

---

## Referensi

- https://docs.python.org/3/
- https://roadmap.sh/python
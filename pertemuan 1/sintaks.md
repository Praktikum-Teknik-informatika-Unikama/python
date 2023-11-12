# Aturan Penulisan Sintaks python

## Penulisan Statement Python

Statement adalah sebuah intruksi atau kalimat perintah yang akan dieksekusi oleh komputer.

Contoh : 

```python
print("Hello World!")
print("Praktikum Pemograman Dasar")
nama = "teknik Informatika"
```

Di bahasa pemogram python Penulisan satu statement tidak diakhiri dengan tanda titik-koma.

tetapi ketika kita mau menuliskan beberapa statemen di satu baris, harus kita pisahkan dengan koma

```python
print("Hello"); print("World"); print("Praktikum pemograman dasar")
nama_depan = "teknik"; nama_belakang = "informatika"
```

## Penulisan String pada Python

String adalah teks atau kumpulan dari karakter.
String dalam pemrograman biasanya ditulis dengan dibungkus menggunakan tanda petik.
Bisa menggunakan tanda petik tunggal maupun ganda.

Contoh:

```python
judul = "Belajar Pemograman dasar menggunakan python"
penulis = 'asprak'
```
Atau kita juga bisa menggunakan triple tanda petik.

Contoh:
```python
judul = """teknik Informatika"""
penulis = '''anjayani'''
```

## Penuilsan Case pada Python

Sintak Python bersifat case sensitive, artinya **teksini** dengan **TeksIni** dibedakan.

Contoh : 

```python
praktikum = "Praktikum pemograman dasar menggunakan python"
Praktikum = "praktikum python"
```

## Case Style

 berikut ini contoh penulisan case yang disarankan: 

```python
    ## Snake Case digunakan pada:
    module_name, package_name, method_name, function_name, , global_var_name, instance_var_name, function_parameter_name, local_var_name.

    ## CamelCase digunakan Pada:
    ClassName, ExceptionName

    ## ALL CAPS digunakan Pada:
    GLOBAL_CONSTANT_NAME
```

## Cara penulisan komentar di python

Komentar merupakan baris kode yang tidak akan dieksekusi \
di python ada bebrapa cara untuk membuat komentar 

- tanda pagar ( # )
- tanda petik ( ",' )
- tanda triple tanda petik ( """,''' )

contoh : 

```python
    
    # ini adalah komentar
    # Ini juga komentar

    "Ini adalah komentar dengan tanda petik ganda"
    'Ini juga komentar, tapi dengan tanda petik tunggal'

    """kelas pagar untuk membuat objek pagar. Dibuat oleh Petani Kode sebagai contoh saja."""
    
```
# Logika Percabangan

Logika percabangan akan mengambil dan memutuskan sesuatu dari sebuah pernyataan dan kemudian menghasilkan sebuah pernyataan jika suatu solusi dapat dipenuhi. Sebagai contoh, ``jika ``, dalam contoh kodenya adalah:

```python
cuaca = "hujan"
if cuaca == "hujan":
    print("gunakan payung")
```

Contoh di atas merupakan contoh sederhana dari logika percabangan dimana jika cuaca hujan maka akan menggunakan payung, dan bagaimana jika value dari ``"huja jika kamu kehujanan maka kamu menggunakan payung"`` kita ganti dengan cerah?.

Jika kita mengganti variabelnya dari ``cuaca = "hujan"``, maka program tidak menghasilkan apapun karena tidak membuat sebuah fungsi atau operator apapun jika ``cerah``, maka untuk membuat fungsi atau operator logika agar dapat mengambil data value berupa ``jika cerah maka tidak menggunakan payung``.

```python
cuaca = "cerah"
if cuaca == "hujan":
    print("gunakan payung")
# menggunakan fungsi elif
elif cuaca == "cerah":
    print("tidak menggunakan payung")
```

Contoh di atas merupakan contoh sederhana dari logika percabangan dimana jika cuaca cerah maka tidak menggunakan payung, dan bagaimana jika value dari ``"cerah"``, ``"hujan"`` kita ganti dengan bebas?

```python
# membuat variabel dari cuaca
# dan membuat value "cerah"
cuaca = "cerah"
# logika jika cuaca hujan
if cuaca == "hujan":
    print("gunakan payung")
# menggunakan fungsi elif
# jika cuaca cerah
elif cuaca == "cerah":
    print("tidak menggunakan payung")
# menggunakan else jika kedua fungsi tidak terpenhi
# if dan elif
else:
    print("gunakan pakaian renang")
```

Contoh diatas merupakan contoh sederhana dari logika percabangan dimana jika selain dari cuaca hujan dan cerah maka menampilkan ``gunakan pakaian renang``.

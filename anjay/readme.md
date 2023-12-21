## For

Contohnya:

```python
angka = [1,2,3,4,5]

for item in angka:
    print(item)
```

Jadi maksud dari koding di atas adalah untuk setiap item di dalam list angka, silahkan tampilkan item tersebut.

Kita juga bisa menggunakan `break` di perulangan `for`:

```python
for item in angka:
    print(item)
    if item == 3:
        break
```

Meskipun statement dari `break` for loop ini beda dengan while loop, maknanya sama saja, kalau itemnya udah di angka 3, break aja, atau selesaikan aja.

apa di for loop ada ```continue```? pastinyaa:

```python
for item in angka:
    if item == 3:
        continue
    print(item)
```

Penjelasannya adalah, apabila item dari list angka tersebut udah ada di angka `3`, angka `3` nya diskip, dan berlanjut ke angka 4.

Last but not least,

```else``` statement

```python
for item in angka:
    print(item)
else:
    print("Selesai !")
```


Apa sih perbedaan antara while loop dan for loop?

- while loop itu bergerak/melakukan sesuatu berdasarkan "kondisi" seperti misalnya tadi, "jika nilai a masih dibawah 5, maka tampilkan a", tapi kalau tidak? tentu outputnya tidak ada lagi dan while loop selesai, hal ini bisa di dukung dengan arti dari ```while``` yang artinya ```ketika```.

- for loop adalah looping yang melakukan sesuatu berdasarkan "keanggotaan", seperti misalnya, "untuk setiap anggota dari list angka, tampilkan (print)", hal ini tentu di dukung dengan arti dari statement for loop yaitu ```for item in iterable``` yang artinya ```untuk setiap item yang ada di dalam iterable``` dan arti kata ```for``` itu sendiri yang artinya ```untuk```.


<a href="https://github.com/bellshade/Python/blob/task/loop/Basic/looping/while_loop.py">while loop</a><br>
<a href="https://github.com/bellshade/Python/blob/task/loop/Basic/looping/for_loop.py">for loop</a>

Video penjelasan tentang looping (for) = [Belajar dasar python - for loop (perulangan)](https://www.youtube.com/watch?v=Z4qfMhx4XzQ&list=PLZS-MHyEIRo59lUBwU-XHH7Ymmb04ffOY&index=25)

Video penjelasan tentang looping (while) = [Belajar dasar python - while loop (perulangan)](https://www.youtube.com/watch?v=ZupffvoCChQ&list=PLZS-MHyEIRo59lUBwU-XHH7Ymmb04ffOY&index=26)

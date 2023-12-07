"""
"230403010005"
"panjang alas di ambil dari kode angkatan di nim"
alas = 23

"ukuran tinggi di ambil dari kode unik angka dari nim (kalo depannya 0 cukup masukkan angka terakhir)"
tinggi = 5

"hitung luas segitiga"
"tampikan luas segita"
"ubah hasilnya integer"
"cek apakah bilangan genap"
"""

"230403010005"
alas = 23
tinggi = 5

luas_segitiga = 1/2 * 23 * 5
print(luas_segitiga)
luas_segitiga = int(luas_segitiga)

if luas_segitiga % 2 == 0 : 
    print("genap")
else : 
    print(luas_segitiga, "ganjil")
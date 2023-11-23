"230403010005"

"panjang alas di ambil dari kode angkatan di nim"
a = 23

"ukuran tinggi di ambil dari kode unik angka dari nim (kalo depannya 0 cukup masukkan angka terakhir)"
t = 5

"hitung luas segitiga"
l_segitiga = 1/2 * a * t

"tampikan luas segita"
print(l_segitiga)

"ubah hasilnya integer"
l_segitiga = int(l_segitiga)

"cek apakah bilangan genap atau ganjil"
l_segitiga = l_segitiga % 2 == 0

print(l_segitiga)

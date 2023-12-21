
BUlAN = 12
BUlAN_LAHIR = 5 # bulan lahir anda

"""
cek selisih antara varibale bulan dan bulan lahir anda,
cek apakah hasil selisih genap atau ganjil  
gunakan if else dan tampilkan selisihnya juga
"""

selisih = BUlAN - BUlAN_LAHIR

if selisih % 2 == 0 : 
    print("selisih bulan lahir saya : {}, genap".format(selisih))
else : 
    print("selisih bulan lahir saya : {}, ganjil".format(selisih))

"nim = 2134"
UNIQUE_NIM = 34

"""
cek jika lebih kecil 25 maka tampilkan "awal" 
cek jika lebih besar atau sama dengan 25 dan lebih kecil 50  maka tampilkan "tengah" 
cek jika lebih besar atau sama dengan 50 dan lebih kecil 70  maka tampilkan "akhir"
jika tidak sesuai dengan kondisi diatas maka tampilkan "nim tidak valid"
"""

if UNIQUE_NIM < 25 : 
    print("awal")
elif UNIQUE_NIM >= 25 and UNIQUE_NIM < 50 :
    print("tengah")
elif UNIQUE_NIM >= 50 and UNIQUE_NIM < 70 :
    print("akhir")
else : 
    print("nim tidak valid")
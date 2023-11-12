"""
buat inputan :
nama
nim
prodi
lalu tampilkan hasil inputan dengan menerapkan string formater versi 3
"""

# membuat variable untuk menampung inputan
nama = input("masukkan nama anda : ")
nim = input("masukkan nim anda : ")
prodi = input("masukkan program studi anda : ")

# print inputan yang sudah kita simpan di variable
print("====================================")
print("nama \t: {}".format(nama))
print("nim \t: {}".format(nim))
print("prodi \t: {}".format(prodi))
# print("nama \t: {} \nnim \t: {} \nprodi \t: {}".format(nama,nim,prodi))
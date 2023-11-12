"""cara penulisan variable di python"""

# variable yang mengandung satu kata
nama = "Aufal"

# variable yang mengandung dua kata atau lebih menggunakan case style snake case
nama_perguruan_tinggi = "Universitas PGRI Kanjuruhan Malang"

# variable yang mengandung dua kata atau lebih menggunakan case style Camel case
namaPerguruanTinggi = "Universitas PGRI Kanjuruhan Malang"


"""Main type data di python"""

# Integer [-2, -1, 0, 1, 2, 3, 4, 5]
type_data_integer = 1234567890
print("Ini type data dari varibale type_data_integer : ",type(type_data_integer)) 

# Float [ -1.25, -1.0, --0.5, 0.0, 0.5, 1.0, 1.25]
type_data_float = 6.809 
print("Ini type data dari varibale type_data_float : ", type(type_data_float))


# String [ "hallo", "hay", "apa kabar"]
type_data_string = "hallo praktikum"
print("Ini type data dari varibale type_data_string : ",type(type_data_string))


""" String di python """

# membuat string menggunakan tanda petik ("")
mata_kuliah = "pemograman dasar"

# membuat string menggunakan tanda petik ('')
mata_kuliah = 'pemograman dasar'

# membuat string menggunakan triple tanda petik ("""""")
mata_kuliah = """pemograman dasar"""

# string formater
nama = "aufal"
umur = 20
# string formater versi pertama
print("nama saya %s" %nama)
# string formater versi kedua
print(f"nama saya {nama}")
# string formater versi ketiga
print("nama saya {}".format(nama))

# menggabungkan string
string1 = "mata "
string2 = "kuliah"
matkul = string1 + string2
print(matkul)
# outpute : mata kuliah

# membuat banyak string yang sama dengan operator(*)
print("string with operator \n" * 3)


""" Input / Output di python """
# nama = input("masukkan nama anda: ")
print("selamat datang " + nama)


""" Back slash """
# \n : enter / new line
# \b : backspace
# \t : tab horizontal

print("nama saya\t: aufal")
print("nama saya\b: aufal")
print("nama saya\n: aufal")



"Percabangan"

angka = 4
cuaca = "cerah"

if  (2 + 2) == 4 or (cuaca == "mendung") : 
    print("benar")
else : 
    print("salah")

match cuaca : 
    case "cerah ": 
        print("jangan pakai payung")
    case "mendung" : 
        print("jangan keluar rumah")
    case _ : 
        print("tidur")


"""
List adalah urutan elemen yang dapat diubah,
sementara tuple adalah urutan elemen yang tidak dapat diubah
"""

#  list
list = ["satu","dua",1,"empat"]

#  tuple
tuple = (1,2,"2",4)

#  dictionary
dictionary = {"satu":1,"dua":2,"tiga":3,"empat":4}


print("hasil : ", tuple[2])
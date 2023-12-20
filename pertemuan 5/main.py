from ast import Break


mahasiswa_list = [
    {
        "nama": "bilhaq",
        "data": {
            "nama_panggilan": "sahatmojo",
            "nim": 230403010005,
            "kampus": "unikama",
            "lulusan_tahun": 2022,
            "prodi": "Informatika",
            "ipk": 3.75
        }
    },
    {
        "nama": "aufal marom",
        "data": {
            "nama_panggilan": "kak aufal",
            "nim": 2123,
            "kampus": "unikama",
            "lulusan_tahun": 2020,
            "prodi": "Sistem Informasi",
            "ipk": 3.85
        }
    },
    {
        "nama": "jane doe",
        "data": {
            "nama_panggilan": "jane",
            "nim": 230403010006,
            "kampus": "unikama",
            "lulusan_tahun": 2023,
            "prodi": "Teknik Elektro",
            "ipk": 3.92
        }
    },
    {
        "nama": "alicia keys",
        "data": {
            "nama_panggilan": "alicia",
            "nim": 230403010023,
            "kampus": "unikama",
            "lulusan_tahun": 2022,
            "prodi": "Ilmu Komunikasi",
            "ipk": 3.78
        }
    },
    {
        "nama": "steve jobs",
        "data": {
            "nama_panggilan": "steve",
            "nim": 230403010045,
            "kampus": "unikama",
            "lulusan_tahun": 2020,
            "prodi": "Teknik Kimia",
            "ipk": 3.89
        }
    },
    {
        "nama": "brad pitt",
        "data": {
            "nama_panggilan": "brad",
            "nim": 230403010089,
            "kampus": "unikama",
            "lulusan_tahun": 2020,
            "prodi": "Akuntansi",
            "ipk": 3.68
        }
    }
]

print("nim : 2134 / ggenap")
for mhs in mahasiswa_list : 
    nim = str(mhs["data"]["nim"])
    if int(nim[-2:]) % 2 == 0 :
        print("nim  genap: ", nim, " nama : ",mhs["nama"])
    # elif (int(nim[-2:]) % 2 == 0) :
    #     print("nim  genap: ", nim, " nama : ",mhs["nama"])
    



""""
Hitung lah tahun pensiun anda berdasarkan patokan umur pensiun, 
patokan diperoleh dari unik nim + 60

tahun berapakah anda pensiun? (jumlahkan (selisih
patokan tahun pensiun dan usia anda), dengan tahun 2023)

example : 
var constan 
    unik_nim : 34
    patokan_pensiun : unik_nim + 60

parameter : tahun lahir
output : tahun pensiun
"""

"hitung_pensiun(2004)"
"prose"
"tahun pensiun : 2098"


unik_nim = 34
patokan_pensiun = unik_nim + 60

def hitung_pensiun(tahun_lahir) : 
    umur = 2023 - tahun_lahir
    selisih = patokan_pensiun - umur
    return 2023 + selisih






def ubah_kurs(jml_uang, mata_uang) :
    if mata_uang == "dolar" :
        return "$ " + str(jml_uang / 15527)
    elif mata_uang == "ringgit" :
        return "MYR " + str(jml_uang / 3335)
    else : 
        print('Mata uang tidak ada')
        exit()

print(ubah_kurs(15000, "ringgit"))
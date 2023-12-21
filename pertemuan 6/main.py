# def sapa(nama):
#     print('hallo', nama)

# def sum(a,b) :
#     print("hasil :", a+b)

# def menyapa(*orang) : 
#     return 'hallo '+ orang[-1]
    
# def ujicoba() :
#     print("ini adalah uji coba")

# def mau_mencoba(satu, dua):
#     A=satu+dua
#     print("A adalah=",A)

# # sapa("febri")
# # sum(3,5)
# # print(menyapa("bili", "febri", "bagus", "vira"))
# # ujicoba()
# mau_mencoba(2,5)

def piramid(angka) :
    for i in range(angka+1) :
        for a in range(i) :
            print('*', end = '')

        print('')

piramid(5)
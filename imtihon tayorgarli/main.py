#class bn ishlash
'''class Noutbuk:
    def __init__(self, nomi,markasi,tez_hotirasi,d_hotirasi,narxi):
        self.nomi = nomi
        self.markasi = markasi
        self.tez_hotirasi = tez_hotirasi
        self.d_hotirasi = d_hotirasi
        self.narxi = narxi

HP = Noutbuk("HP","Pavilion","BGb","1Tb","750$")
print(HP.nomi)
print(HP.tez_hotirasi)
'''


#2 variant 3 inchi savol ga javob
'''yangi_sonlar = []
sonlar = [10,20,30,40,50,60]
for i in sonlar:
    i += 6
    yangi_sonlar.append(i)
print(yangi_sonlar)'''

#File la bn ishlash , 4 inchi sovolga javob
'''with open("yakshanbada_kelganlar.doc", "w") as file:
    file.write("Sardor, Abdujalil, Ubaydulo, Ismoil, Imron, Firdavz")

file.close()
'''

#3 variant ning sovollari
'''def Harf_sanash(matn):
    bosh, kichik, raqamlar = 0, 0, 0
    for i in range(len(matn)):
        if matn[i].isupper():
            bosh +=1
        elif matn[i].islower():
            kichik += 1
        #isdigit raqamlar ni sanaydi
        elif matn[i].isdigit():
            raqamlar += 1

    print('Bosh harflar:',bosh, "ta")
    print('kichik harflar:',kichik, "ta")
    print(f"Raqamlar: {raqamlar} ta ")

matn = input("Matnni kiriting: ")

Harf_sanash(matn)
'''


#3 VARIANTNING 4 MASALA SI


'''for i in range(0,5):
    kod = input("kodni kiriting:")
    if kod=="mars@2021":
        print("welcom")
        break
    elif kod!="mars@2021" and i<4:
        print("notogri kirittingiz")
    else:
        print("Urunishlar soni tugadi")
'''

input("matinni kiriting")




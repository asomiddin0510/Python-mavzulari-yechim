"""
Dasturni modullarga bo'lish
"""


"""Funksiya
	

Funksiya ta'rifi

ceil(x)
	

x dan katta yoki teng bo'lgan eng kichik butun sonni qaytaradi

fabs(x)
	

x ning absolyut qiymatini qaytaradi

floor(x)
	

x dan kichik yoki teng bo'lgan eng yaqin butun sonni qaytaradi

exp(x)
	

xexe ni qaytaruvchi funksiya

cos(x)
	

cos⁡(x)cos(x) ni qaytaruvchi funksiya

sin(x)
	

sin⁡(x)sin(x) ni qaytaruvchi funksiya

tan(x)
	

tan⁡(x)tan(x) ni qaytaruvchi funksiya

degrees(x)
	

x burchakning radian qiymatini darajaga konvertasiya qilish

radians(x)
	

x burchakning daraja qiymatini radianga konvertasiya qilish 

e
	

Matematik konstanta ee (2.71828...)"""


# from modul import avto_royxat, royxat_chiqar, royxatni_tuz
#
# rezult = royxatni_tuz()
# royxat_chiqar(rezult)


# import math
#
# ildiz = math.sqrt(121)
# print(ildiz)


# daraja = math.pow(12, 2)
# print(daraja)


# log = math.log2(8)
# print(log)


# pi_saqla = math.pi
# print(pi_saqla)


# katta_butun = math.ceil(21.23)
# print(katta_butun)



# katta_butun = math.ceil(23.1)
# print(katta_butun)



# absalyut = math.fabs(-12.12)
# print(absalyut)



# absalyut = math.fabs(-23)
# print(absalyut)


# absalyut = abs(-12.12)
# print(absalyut)



# kichik_butun = math.floor(12.12)
# print(kichik_butun)




"""
Random moduli tasodifiy sonlar bilan ishlash uchun qulay funksiyalarga boy. Keing ulardan ayrimlari bilan tanishamiz.
"""

import random as ran

"""
randint(a,b)

Bu funksiya a va b oraligi'da tasodifiy butun son qaytaradi. 
"""

"""choice(x)

x ning ichidan tasodifiy qiymatni qaytaruvchi funksiya. Bunda x bir necha elementdan iborat o'zgaruvchi (matn, ro'yxat) bo'lishi kerak."""


# son = ran.randint(0, 100)
# print(son)


# def son_qaytar() :
#     son = int(input("Assalomu alaykum men sizga malum bir oraliqdan sonni tanlab beraman boshlanish nuqtani kiriting : "))
#     son1 = int(input("Tugash nuqtasni kiriting : "))
#     return ran.randint(son , son1)
#
# tanlangan = son_qaytar()
# print(tanlangan)





# def son_qaytar(son, son1):
#     return ran.randint(son, son1)
#
# son = int(input("Assalomu alaykum men sizga ma'lum bir oraliqdan sonni tanlab beraman, boshlanish nuqtani kiriting: "))
# son1 = int(input("Tugash nuqtasini kiriting: "))
# tanlangan = son_qaytar(son, son1)
# print(tanlangan)



# ismlar = ['Abror', 'Alisher', 'Asommiddin', 'Bobur']
# ism = ran.choice(ismlar)
# print(ism)


# def royxatichidan_tanla(royxat) :
#     return ran.choice(royxat)
# ismlar = ['Abror', 'Alisher', 'Asommiddin', 'Bobur']
# print(royxatichidan_tanla(ismlar))



# def kiritilgandan_tanla() :
#     royxat = []
#     while True :
#         ism = input("Istalgan insoning ismini kiriting: ")
#         royxat.append(ism)
#         savol = input('Yana kiritishni istaysizmi (ha/yo\'q) : ')
#         if savol.lower() != 'ha' :
#             break
#     return f"Siz kiritgan ro'yxat: {royxat} va tanlangan ism : {ran.choice(royxat)}"
#
# print(kiritilgandan_tanla())




# royhat = list(range(1, 100, 4))
# tanla = ran.choice(royhat)
# print(f"Siz kiritgan: {royhat} gacha bo'lgan sonlardan tanlangan son : {tanla} ")



# sonlar = list(range(1, 25))
# print(sonlar)
#
# ran.shuffle(sonlar)
# print(sonlar)


import random as ran


# def arlashtir() :
#     sonlar = []
#     while True :
#         son  = int(input('Son kiriting : '))
#         sonlar.append(son)
#         savol = input('Yana son kiritasizmi (ha/yo\'q) : ')
#         if savol.lower() == 'yo\'q' :
#             break
#     ran.shuffle(sonlar)
#     return sonlar
#
# print(arlashtir())































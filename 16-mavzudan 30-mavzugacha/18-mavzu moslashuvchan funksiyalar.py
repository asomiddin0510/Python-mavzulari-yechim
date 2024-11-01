"""

MOSLASHUVCHAN FUNKSIYA (*args, **kwargs)

"""



""" *args """
# def summa(*sonlar) :
#     yigindi = 0
#     for son in sonlar :
#         yigindi += son
#     return yigindi
#
# sonlaryigindi = summa(1, 2, 3, 4, 5, 6, 7, 8, 9)
# print(sonlaryigindi)
# print(summa(9, 3, 29, 4, 8, 5, 19, 34 ))



#
# def yigindi(x, y, *sonlar) :
#     yigindi_yi = 0
#     for son in sonlar :
#         yigindi_yi += son
#     return y + x + yigindi_yi
# print(yigindi(1, 5, 4, 3, 8, 9))



# def afto_info(kompaniya, modeli, **malumotlari) :
#     malumotlari['Kompaniya'] = kompaniya,
#     malumotlari["Model"] = modeli
#     return malumotlari
# afto_1 = afto_info('GM' , 'Kaptiva'     , rangi = 'qora', narxi = 23, turi = 'aftomat')
# afto_2 = afto_info('GM', 'Malibu', rangi = 'Oq', narxi = 28 , turi = 'Mexanik')
# print(afto_2)
# print(afto_1)



# 1.Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing
# def kopaytma(*sonlar) :
#     kopaytma_yig  = 1
#     for son in sonlar :
#         kopaytma_yig *= son
#     return kopaytma_yig
# print(kopaytma(2, 4, 6, 9, 8))



# 2.Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozing.
# Talabaning ismi va familiyasi majburiy argument, qolgan ma'lumotlar esa ixtiyoriy ko'rinishda istalgancha berilishi mumkin bo'lsin.
# def talaba_malumot(ism, familya, **malumotlar) :
#     malumotlar["Ismi"] = ism,
#     malumotlar["Familya"] = familya,
#     return malumotlar
# malumot_talaba = talaba_malumot("Asomiddin", "Abduqahharov", kursi = 2, fakulteti = "Axborot texnalogiyalar", yonalis = 'Kampyuter injnering')
# malumot_talaba1 = talaba_malumot("Alisher", "Abdullayev", kursi = 3, fakultet = 'Matematika', yonalish = 'Matimateka analiz')
# print(malumot_talaba)
# print(malumot_talaba1)



# def talaba(ism, familya, baho , **malumot) :
#     malumot['Ismi'] = ism,
#     malumot['Familyasi'] = familya,
#     malumot["Bahosi"] = baho
#     malumot
#     return malumot
# malubot = talaba("Asomiddin", "Abduqahharov", 5, yonalish = "Kampyuter injneringi", fakulteti = "Axborot")
# for key, value in malubot.items() :
#     print(key, value)




# 1-masala.
# Berilgan so'zlardan eng uzunini topadigan funksiya yozing (*args ishlatilsin).
# def uzun_qay(*sozlar) :
#     qiy = []
#     for soz in sozlar:
#         qiy.append(len(soz))
#     return  max(qiy)
# print(uzun_qay('salom12', 'men', 'olma12122', 'anor', 'qovun', 'tarvuz'))



# 2-masala
# Argumentlar orasidan faqat juft sonlarni qaytaradigan funksiya tuzing (*args bilan).
# def juft_qay(*sonlar) :
#     juft = []
#     for son in sonlar :
#         if son % 2 == 0 :
#             juft.append(son)
#     return juft
# print(juft_qay(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ,13, 14, 15))




# 3-masala.
# Har xil turdagi ma'lumotlarni qabul qilib, ularning turini aniqlaydigan funksiya yarating (*args orqali).
# def tur_qay(*malumotlar) :
#     turlar = []
#     for malumot in malumotlar :
#
#         turlar.append(type(malumot))
#
#     return turlar
#
# print(tur_qay('salom', 'men', 12, 23.3, -23, (-1)**0.5))




# 4-masala.
# Berilgan sonlar orasidan eng kattasini topadigan funksiya yozing (*args ishlatilsin).
# def katta_qaytar(*sonlar) :
#     return max(sonlar)
# print(katta_qaytar(12, 3, 2, 34, 21, 35, 45, 56, 26))




# 5-masala.
# Barcha argumentlarni birlashtirib, bitta satrga aylantiradigan funksiya tuzing (*args bilan).
# def sat_birlashtir(*matnlar) :
#     return " ".join(matnlar)
#
# print(sat_birlashtir('salom', 'men', 'asomiddin' , 'yoshdaman'))




# 6-masala.
# Foydalanuvchi ma'lumotlarini saqlaydigan funksiya yarating (**kwargs yordamida).
# def foydalanuvchi_data(**malumotlar) :
#     return malumotlar
# print(foydalanuvchi_data(ismim = 'Asomiddin', familyam = 'Abduqahharov', yoshi = 19, Yashash_joyim = 'Bandixon' ))




# 7-masala.
# Lug'atni yangilaydigan funksiya tuzing (**kwargs orqali).
# def yangi_lugat(**lugat) :
#     while True :
#         savol = input("Qaysi lug'atni yangilamoqchisiz <key>ni kiriting: ")
#         savol1 = input(f"{savol} ning valuesni kiriting: ")
#         lugat[savol] = savol1
#         savol2 = input("Agar dasturni tugatishni istsangiz 'exit' ni yozing ")
#
#         if savol2 == 'exit' :
#
#             break
#     return lugat
# print(yangi_lugat())





# 8-masala.
# Lug'atni yangilaydigan funksiya tuzing (**kwargs orqali).


# def lugat_ozgart(**lugatlar) :
#
#     while True :
#
#         savol = input("Siz lug'at qo'shishni istasangiz 'append' deb kiriting \nMavjud ro'yxatni o'zgartrishni istasangiz 'change' deb yozing : ")
#
#         if savol.lower() == 'append' :
#
#             key = input("Nima qo'shmoqchi bo'lsangiz birinchi bo'lib kalitni kiriting : ")
#             value = input(f"{key} ning qiymatni kiriting : ")
#
#             lugatlar[key] = value
#
#
#         elif savol.lower() == 'change' :
#
#             key_oz = input("O'zgartirmoqchi bo'lgan elementingizni kalitini kiriting : ")
#             if key_oz in lugatlar :
#                 oz_key = input(f"{key_oz} ni nimaga o'zgartirmoqchisiz kalit kiriring : ")
#                 oz_value = input(f"{oz_key} ning qiymatni kiriting : ")
#                 lugatlar[oz_key] = oz_value
#
#             else:
#                 yoq_key = input(f"{key_oz} nomli kalit yoq qiymatni kiriting: " )
#                 lugatlar[key_oz] = yoq_key
#
#         savol2 = input("Dasturni to'xtatishni istasangiz 'stop' deb yozing : ")
#         if savol2.lower() == 'stop' :
#                 break
#     return lugatlar
#
#
# lugatlar = lugat_ozgart()
# for soz in lugatlar.items() :
#     print(soz)































































































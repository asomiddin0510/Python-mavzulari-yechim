"""
Nomsiz funksiyalar lambda, map, filter funksiyalar
"""
import math
from functools import reduce



# uzunlik = lambda r , pi : 2 * pi * r
# print(uzunlik(10, math.pi))



# kvadrat = lambda x, y : x ** y
# print(kvadrat(5, 2))


# def daraja(n) :
#     return lambda x : x ** n
# kvadrat = daraja(2)
# print(kvadrat(9))

# kub = daraja(3)
# print(kub(7))



#  Ro'yxatdagi so'zlarni uzunligi bo'yicha tartiblash:
 #       Lambda funksiyasini sorted funksiyasi bilan birgalikda foydalanib, ro'yxatdagi so'zlarni uzunligi bo'yicha tartiblang.
sozlar = ['salomni', 'olcha', 'so\'zlar', 'keling', 'narmanli', 'natija', 'qiymat']
sort_sozlar = {}
for soz in sozlar :
    sort_sozlar[soz] = len(soz)
print(sort_sozlar)
rezult = sorted(sort_sozlar)
print(rezult)



"""map() funksiyasiga doir masalalar:"""

#Kvadratini hisoblash:
#Lambda funksiyasini yozing, u berilgan sonning kvadratini qaytaradi.

# kvadrat = lambda x : x ** 2
# x = int(input('Son kiriting : '))
# print(f"Siz kiritgan {x} ning kvadrati : {kvadrat(x)} ga teng")
# print(kvadrat(23))



#     Ikki sonni qo'shish:
#         Lambda funksiyasini yozing, u ikkita sonni qo'shadi.
# yigindi = lambda x, y : x + y
# print(yigindi(21, 24))



#    Ikki sonning kattasini aniqlash:
#        Lambda funksiyasini yozing, u ikkita sonning kattasini qaytaradi.
# katta = lambda x, y : x if x > y else y
# print(katta(23, 33))

# katta = lambda x, y, z : f"{x} eng kattasi" if x > y and x > z  else (f"{y} eng kattasi" if (y > x and y > z) else f"{z} eng kattasi")
# print(katta(1, 13, 6))





#   Berilgan sonning juft yoki toq ekanligini aniqlash:
#   Lambda funksiyasini yozing, u berilgan sonning juft yoki toq ekanligini aniqlaydi.
# aniqla = lambda a : f"Siz kiritgan {a} soni juft son" if a % 2 == 0 else f"Siz kiritgan {a} soni toq son"
# a = int(input('Son kiriting: '))
# print(aniqla(a))





# Berilgan sonning musbat yoki manfiy ekanligini aniqlash:
#       Lambda funksiyasini yozing, u berilgan sonning musbat yoki manfiy ekanligini aniqlaydi.
# aniqla = lambda x : f"Siz kiritgan {x} soni musbat" if x > 0 else f"Siz kiritgan {x} soni manfiy "
# son = int(input('Son kiriting: '))
# print(aniqla(son))




#    Berilgan so'zning uzunligini aniqlash:
#        Lambda funksiyasini yozing, u berilgan so'zning uzunligini qaytaradi.

# uzunlik = lambda soz : len(soz)
# soz = input("Soz kiritng : ")
# print(uzunlik(soz))




#    Ro'yxatdagi barcha elementlarning kvadratlarini hisoblash:
 #       Lambda funksiyasini map funksiyasi bilan birgalikda foydalanib, ro'yxatdagi barcha elementlarning kvadratlarini hisoblang.
# sonlar = list(range(1, 30))
# kvadrat = map(lambda x : x**2 , sonlar)
# print(list(kvadrat))




#    Ro'yxatdagi juft sonlarni filtrlaydigan lambda funksiyasi:
 #       Lambda funksiyasini filter funksiyasi bilan birgalikda foydalanib, ro'yxatdagi juft sonlarni filtrlang.
# sonlar = list(range(1, 38))
# juft_sonlar = list(filter(lambda son : son % 2 == 0, sonlar))
# print(juft_sonlar)





 #   Ro'yxatdagi barcha elementlarni ikki barobar oshiradigan lambda funksiyasi:
#        Lambda funksiyasini map funksiyasi bilan birgalikda foydalanib, ro'yxatdagi barcha elementlarni ikki barobar oshiring.
# royhat = ['olma', 'anor', 'shaftoli', 'banan', 'gilos', 'sabzi', 2, 5, 8]
# ikki_barobar = map(lambda buyum : [buyum, buyum], royhat)
# print(list(ikki_barobar))




#    Ro'yxatdagi sonlarning yig'indisini hisoblash:
#        Lambda funksiyasini reduce funksiyasi bilan birgalikda foydalanib, ro'yxatdagi sonlarning yig'indisini hisoblang.
# sonlar= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# yigindi = reduce(lambda x, y: x+y, sonlar)
# print(yigindi)




#    Ro'yxatdagi eng katta sonni aniqlash:
#        Lambda funksiyasini reduce funksiyasi bilan birgalikda foydalanib, ro'yxatdagi eng katta sonni aniqlang.
#
# sonlar = [6, 39, 5, 10, 23, 37, 28, 38, 30]
# eng_katta = reduce(lambda x, y : x if x > y else y, sonlar)
# print(eng_katta)



#
  #  Kvadratlar:
 #       Berilgan ro'yxatdagi barcha elementlarning kvadratini hisoblang.
#        Masalan: [1, 2, 3, 4] -> [1, 4, 9, 16]
# sonlar = [11, 21, 32, 24, 15, 6, 27, 8, 19, 10]
# kv = list(map(lambda son : son **2, sonlar))
# print(kv)




#    Katta harflar:
 #       Berilgan ro'yxatdagi barcha matn elementlarini katta harflarga aylantiring.
#        Masalan: ['olma', 'anor'] -> ['OLMA', 'ANOR']

# royhat = ['olma', 'anor', 'shaftoli', 'anjir', 'banan', 'olcha']
# rezult = list(map(lambda meva : meva.upper(), royhat))
# print(royhat ," --->>> ", rezult)




#    Ikki barobar:
 #       Berilgan ro'yxatdagi barcha raqamlarni ikki barobar oshiring.
#        Masalan: [1, 2, 3, 4] -> [2, 4, 6, 8]
# royxat = [1, 2, 3, 4, 'salom', 'matn', 5, 6, 7, 'hello', 'termiz', 8, 9]
# rezult = list(map(lambda element : 2 * element if isinstance(element, int) else element, royxat))
# print(rezult)





#    String uzunligi:
 #       Berilgan ro'yxatdagi barcha matn elementlarining uzunligini hisoblang.
#        Masalan: ['olma', 'anor'] -> [4, 4]
# royhat = ['salom', 'matn', 'olma', 'olcha', 'banan', 'shaftoli']
# rezult = list(map(lambda element : len(element), royhat))
# print(rezult)



#    Kelishik qo'shish:
 #       Berilgan ro'yxatdagi barcha matn elementlariga "-ni" kelishigini qo'shing.
#        Masalan: ['olma', 'anor'] -> ['olmani', 'anorni']
# royhat = ['anor', 'olma', 'olcha', 'shaftoli', 3, 4, 'sherik', 'matn', 'ish']
# rezult = map(lambda x : str(x) + 'ni' , royhat)
# print(list(rezult))



#    Yuqori quvvat:
 #       Berilgan ro'yxatdagi barcha raqamlarni uchinchi darajaga oshiring.
#        Masalan: [1, 2, 3, 4] -> [1, 8, 27, 64]

# sonlar = list(range(1, 20))
# rezult = map(lambda son : son**3 , sonlar)
# print(list(rezult))






#    Matn takrorlash:
 #       Berilgan ro'yxatdagi barcha matn elementlarini ikki marta takrorlang.
#        Masalan: ['olma', 'anor'] -> ['olmaolma', 'anoranor']
# mevalar = ['olma', 'anor', 'shaftoli', 'olcha', 'banan', 'xurmo']
# rezult = map(lambda meva : meva + meva, mevalar)
# print(list(rezult))




#    Absolyut qiymat:
 #       Berilgan ro'yxatdagi barcha raqamlarning absolyut qiymatini hisoblang.
#        Masalan: [-1, -2, 3, -4] -> [1, 2, 3, 4]
# sonlar = list(range(-20, -2))
# rezult = map(lambda son : abs(son), sonlar)
# print(list(rezult))



# Musbat sonlar:
#     Berilgan ro'yxatdan faqat musbat sonlarni ajratib oling.
#     Masalan: [-1, 2, -3, 4] -> [2, 4]
# sonlar = [-2, 3, 5, -5, 23, -34, 28, -34, -24, 43, 29, -38, 19]
# musbat = list( filter( lambda son : son>0 , sonlar) )
# print(musbat)


# Katta harf bilan boshlanuvchi:
#     Berilgan ro'yxatdan faqat katta harf bilan boshlanuvchi matn elementlarini ajratib oling.
#     Masalan: ['Olma', 'anor', 'Banan'] -> ['Olma', 'Banan']
# royhat = ['Olma', 'anor', 'olcha', 'Banan', 'Gilos', 'Shaftoli', 'Sabzi', 'Tarvuz', 'royhat', 'matn']
# rezult = filter(lambda element :  element[0].isupper() , royhat)
# print(list(rezult))

# rezult = filter(lambda element : element[0].islower(), royhat)
# print(list(rezult))


# Juft sonlar:
#     Berilgan ro'yxatdan faqat juft sonlarni ajratib oling.
#     Masalan: [1, 2, 3, 4] -> [2, 4]
# royhat = list(range(1, 26))
# rezult = list(filter(lambda son : son%2 == 0 , royhat))
# print((rezult))


# 5 dan katta sonlar:
#     Berilgan ro'yxatdan faqat 5 dan katta sonlarni ajratib oling.
 #     Masalan: [1, 6, 3, 8] -> [6, 8]
# royhat = [3, 27, 38, 27, 4, 1, 38, 84, 34, 5, 35, 49, -4, -29, -39, 2, 1.3, 3.4 ]
# rezult = list(filter(lambda son : son > 5 , royhat))
# print(rezult)


# Matn uzunligi 5 dan katta:
#     Berilgan ro'yxatdan faqat uzunligi 5 dan katta bo'lgan matn elementlarini ajratib oling.
#     Masalan: ['olma', 'anor', 'shaftoli'] -> ['shaftoli']
# mevalar = ['olma', 'shaftoli', 'gillos', 'olcha', 'banan', 'hurmo', 'tarvuz', 'qovun']
# rezult = list(filter(lambda meva : len(meva) > 4 and meva[0] == 'o', mevalar))
# print(rezult)


# Bo'sh bo'lmagan matnlar:
#     Berilgan ro'yxatdan faqat bo'sh bo'lmagan matn elementlarini ajratib oling.
#     Masalan: ['', 'anor', '', 'banan'] -> ['anor', 'banan']
#royhat = [' ', 'malumot', 'rejim', ' ', 'forma', 'taxrir', ' ', '', '', 'sdo',   "   "]
#rezult = list(filter(lambda element : element.isupper() and element.islower() , royhat))
# print(rezult)



# Musbat va juft sonlar:
#     Berilgan ro'yxatdan faqat musbat va juft sonlarni ajratib oling.
#     Masalan: [-1, 2, -3, 4] -> [2, 4]
# sonlar = [3, 7, 9, 23, 17, 38, 4, 34, 24, -3, -5, 12, -11, -13, 17, -16, 0, -18]
# rezultat = list(filter(lambda son : son >= 0 and son % 2 == 0, sonlar))
# print(rezultat)


# Matn ichida 'a' harfi bor:
#     Berilgan ro'yxatdan faqat ichida 'a' harfi bor matn elementlarini ajratib oling.
#     Masalan: ['olma', 'anor', 'shaftoli'] -> ['olma', 'anor', 'shaftoli']
# royhat = ['olma', 'anor', 'shaftoli', 'olcha', 'banan', 'tarvuz', 'qovun', 'malum', 'balkim', 'daraxt', 'salkam', 'men', 'sen', 'barcha']
# rezult = list(filter(lambda soz : 'a' in soz, royhat))
# print(rezult)


































"""
Funksiya >>> ro'yxatlar va lug'atlar

"""



# def bahola(ismlar) :
#     talabalar = {}
#     while ismlar :
#         ism = ismlar.pop()
#         baho = int(input(f"Iltimos {ism.title()}ning bahosni kiriting: "))
#         talabalar[ism.title()] = baho
#     return talabalar
# talabalar_royhat = ['asomiddin', 'abror', 'alisher', 'dilshod', 'sherzod', 'sardor']
# baholar = bahola(talabalar_royhat)
# print(f"Baholangan talabalarning ro'yhati va baholari : {baholar}")




# 1. Berilgan sonning kvadratini qaytaruvchi funksiya.
# def kv_qay(a):
#     kv = a ** 2
#     return kv
# kv = kv_qay(20)
# print(kv)



# 2. ikkita sonni qabul qilib ularning yig'indisini print qiluvchi funksiya
# def yigindi(a, b):
#     yig = a + b
#     return yig
# son1 = int(input("Birinchi sonni kiriting: "))
# son2 = int(input("Ikkinchi sonni kiriting: "))
# yigindina = yigindi(son1, son2)
# print(f"{son1} va {son2} ning yig'indisi {yigindina} ga teng")



# 3. Berilgan sonning toq yoki juft ekanligini aniqlovchi funksya
# def aniqloci(son) :
#     if son % 2 == 0 :
#         return f"Siz kiritgan {son} juft son"
#     else:
#         return f"Siz kiritgan {son} toq son"
# savol = int(input('Son kiritng: '))
# son_aniqlovci = aniqloci(savol)
# print(son_aniqlovci)




# 4. Berilgan sonnning musbat yoki manfiy ekanligini aniqlovchifunksiya
# def mus_man(son) :
#     if son > 0 :
#         return f"Siz kiritgan {son} musbat son "
#     else:
#         return f"Siz kiritgan {son} manfiy son"
#
# son = int(input("Son kiriting: "))
# rezult = mus_man(son)
# print(rezult)




# 5. Berilgan songacha bo'lgan sonlarni pprint qiluvchi funksiya.
# M: 9 bo'lsa 1, 2, 3, 4, 5, 6, 7, 8, 9
# def ciqaruci_son(son) :
#     if son >= 0 :
#         a = 0
#         sonlar = []
#         while a < son :
#             a += 1
#             sonlar.append(a)
#         return sonlar
#     else:
#         return  "Siz kirtgan son 0 dan kichik iltimos 0 dan katta son kiriting "
#
# savol = int(input("Son kiriting: "))
#
# ciqar = ciqaruci_son(savol)
#
# for i in ciqar:
#     print(i)

# 6. 2 ta sonni qabul qilib ularning o'rta arifmetifgini qaytaruvchi funkiya. o'rta
# arifmetik (a+b)/2
# def ortaarfmet(son1, son2) :
#     orta = ( son1 + son2 )* 0.5
#     return f"Siz kiritgan {son1} va {son2} ning o'rta arifmetigi {orta} ga teng"
#
# savol1 = int(input("Birinchi sonni kiriting: "))
# savol2 = int(input("Ikkinchi sonni kiriting: "))
#
# result = ortaarfmet(savol1, savol2)
# print(result)


# 7. List qabul qilib uning elemntlarini print qiluvchi funksiya.

# def list_ciqar(royhat) :
#     for i in royhat :
#         print(i)
#
# mevalar = ['olma', 'olcha', 'shaftoli', 'anjir', 'banan', 'ananas', 'qulupnay']
# ciqar = list_ciqar(mevalar)
# print(ciqar)




# 8. List qabul qilib uning elemntlari yig'indisini qaytaruvchi funksiya.
# def yigindi(royhat) :
#     yig = 0
#     for son in royhat :
#         yig += son
#     return yig
#
# sonlar = [1, 3, 5]
#
# yigindi_ciq = yigindi(sonlar)
# print(yigindi_ciq)




# 9. list qabul qilib uning eng kichik eleemntini qaytaruvchi funksiya.
# def min_ciqar(royhat_son) :
#     son =min(royhat_son)
#     return son
# sonlar = [ 4, 8, 40, 38, 24, 59, 19, 39]
# kichik_son = min_ciqar(sonlar)
# print(kichik_son)



# 10. List qabul qilib uning eng katta elementini qaytaruvchi funksiya.
# def katta_ciq(royhat) :
#     son = max(royhat)
#     return son
#
# sonlar = [23, 43, 23, 24, 19, 131, 43, 28, 48, 38]
# katta = katta_ciq(sonlar)
# print(katta)





# 11. List qabul qilib uning elemntlari kvadratlari yigindisini qaytaruvchi funskiya.
# def kv_yigindi(sonlar) :
#     kv_yig = 0
#     for i in sonlar :
#         kv_yig += i ** 2
#     return kv_yig
# sonlar = [2, 4, 3, 5, 6]
# kv = kv_yigindi(sonlar)
# print(kv)





































"""
Funksiya bilan tanishish
"""


# def salom_qay():
#     """Funksiya chaqrilganda salom qaytaruvchi funksiya! """
#     print("Assalomu alaykum")
# salom_qay()



# def salom_qaytar(ism):
#     """Bu funksiya ism olib salom qaytaradi!"""
#     print(f"Assalomu alaykum {ism.title()} ")
# salom_qaytar("Asomiddin")



# def yosh_qaytar(ism, t_yil):
#     """Foydalanuvchidan ism va tug'ilgan yilni olib yoshini qaytaradi!"""
#     print(f"Assalomu alaykum {ism.title()} Sizning yoshingiz: {2024-t_yil} da")
# yosh_qaytar("asomiddin", 2005)
# print(yosh_qaytar.__doc__)



# def ism_familya(ism, familya):
#     print(f"Assalomu alaykum {ism.title()} {familya.title()}")
# ism_familya("asomiddin", 'abduahharov')



#     Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozing.
# def ism_yosh(ism, t_yil):
#     print(f"Assalomu alaykum {ism.title()} yoshingiz {2024-t_yil} da")
# ism_yosh("asomiddin", 2005)




#     Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.
# def kv_kub(a):
#     print(f"Siz kiritgan {a} ning kvadrati {a**2} kubi {a**3} ga teng")
# kv_kub(4)




#     Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.
# def son_turanqlovchi(b):
#     if b%2 == 0 :
#         print(f"Siz kiritgan {b} juft son")
#     else:
#         print(f"Siz kiritgan {b} toq son")
# son_turanqlovchi(23)



#     Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing. Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.
# def katta_son(a, d):
#     if a > d:
#         print(f"Siz kirtgan sonlardan kattasi: {a}")
#     elif a == d:
#         print("Siz kirtgan sonar teng")
#     else:
#         print(f"Siz kirtgan sonlardan kattasi: {d}")
# katta_son(23, 23)




#     Foydalanuvchidan x va y sonlarini olib, xyxyni konsolga chiqaruvchi funksiya yozing.
# def daraja(x, y):
#     print(f"Siz kiritgan {x} ning {y}-darajasi {x**y} ga teng")
# daraja(3, 5)



#     Yuqoridagi funksiyada y uchun 2 standart qiymatini bering.
# def standrd_y(x, y=2):
#     print(f"Siz kirtgan {x} ning {y}-darajasi : {x**y} ga teng")
# standrd_y(4,8)




#     Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya yozing. Natijalarni konsolga chiqaring.

# def son_bol(a):
#
#     bolnadigan = []
#     bolinmaydigan = []
#
#     for i in range(2, 10):
#         if a % i == 0:
#             bolnadigan.append(i)
#         else:
#             bolinmaydigan.append(i)
#     return bolnadigan, bolinmaydigan
#
# bolnadigan, bolinmaydigan = son_bol(20)
#
# print(f"Siz kiritgan son quydagi sonlarga qoldiqsiz bo'lnadi: {bolnadigan} \nBo'linmaydigan sonlar: {bolinmaydigan}")




# Foydalanuvchidan son qabul qilib, sonni 2, 3, 4 va 5 ga qoldiqsiz bo'linishini tekshiruvchi
# funksiya yozing.
# Natijalarni konsolga chiqaring ("15 soni 3 ga qoldiqsiz bo'linadi" ko'rinishida)
# def bolinish(d):
#     bolinuvchilar = []
#     for i in range(2, 6):
#         if d % i == 0:
#             bolinuvchilar.append(f"{d} soni {i} ga qoldiqsiz bo'lnadi")
#     return bolinuvchilar
# bol = bolinish(24)
# for i in bol:
#     print(i)

# def bolinuchilar(d):
#     for i in range(2, 6):
#         if d % i == 0:
#             print(f"{d} soni {i} ga qoldiqsiz bo'linadi! ")
# bolinuchilar(24)



# def toliq_ism(ism, familya, otasning_ismi = " "):
#     if otasning_ismi:
#         tolq = f"Talabaning to'liq ismi familyasi: {ism, familya, otasning_ismi}"
#     else:
#         tolq = f"Talabaning ismi: {ism, familya}"


#
# def aftomobil_jam(nomi, rangi, turi, yoqilgi_sarfi, karobka, yil, narhi = None ):
#     mashina = {
#         'nomi': nomi,
#         'rangi': rangi,
#         'turi': turi,
#         "yoqilg'i sarfi": yoqilgi_sarfi,
#         'karobka': karobka,
#         'yili': yil,
#         'narhi': narhi
#     }
#     return mashina
#
# print("Bizda hozirda bor aftomobillarni holati: ")
#
# mashina1 = aftomobil_jam('gentra', 'qora', 1.6, 12, 'mexanik', 2023, narhi=None)

# mashina2 = aftomobil_jam('Damas', 'oq', '1.8', 10, 'mexanik', 2021, )
# mashina3 = aftomobil_jam('kobolt', 'oq', 2.4, 8, 'aftomat', 2020)
# afto = [mashina1, mashina2, mashina3]
# print(afto)



# def oraliq(min, max):
#     sonlar = []
#     while min < max:
#         sonlar.append(min)
#         min += 1
#
#     return sonlar
# sonlar = oraliq(12, 200)
# for i in sonlar:
#     print(i)


# def oraliq(min , max , qadam = 1):
#     sonlar = []
#     while min < max :
#         min += qadam
#         sonlar.append(min)
#
#     return sonlar
# sonlar = oraliq(0, 80, 4 )
# print(sonlar)




def aftomobil_jam(nomi, rangi, turi, yoqilgi_sarfi, karobka, yil, narhi = None ):
    mashina = {
        'nomi': nomi,
        'rangi': rangi,
        'turi': turi,
        "yoqilg'i sarfi": yoqilgi_sarfi,
        'karobka': karobka,
        'yili': yil,
        'narhi': narhi
    }
    return mashina


cars = []

print("Siz bu dastur orqali mashinalar ro'yhatni tuza olasiz")

while True:
    print("Quydagi savollarni to'ldiring")
    nomi = input("Mashina modeli kiriting: ")
    rangi = input("Rangni kiriting: ")
    turi = input("Turini kiriting: ")
    sarfi_y = input("Yoqilg'i sarfni kiritng: ")
    karobka = input("Karobkasni kiriting: ")
    yili = input("Chiqgan yilni kiriting: ")
    narhi = int(input("Narhni kiritng $ : "))

    cars.append(aftomobil_jam(nomi, rangi, turi, sarfi_y, karobka, yili, narhi))
    savol = input("Davom etishni istaysizmi unda (yes/no) ni kiriting : ")
    if savol.lower() == 'no':
        break

# for mashina in cars:
#     print("Modeli " ,mashina['nomi'], 'rangi ', mashina['rangi'], 'narxi' , mashina['narhi'] ,'ming $')



# Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning birinchi harfini katta harfga o'zgatiruvchi funksiya yozing.































































































































































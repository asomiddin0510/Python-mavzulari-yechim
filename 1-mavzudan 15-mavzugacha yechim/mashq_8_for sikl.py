"""
For takrorlash operatori

"""
from operator import truediv, index

"""
Dasturlash davomida kodimizning biror qismini bir necha marta 
takrorlash talab etilishi mumkin. Misol uchun, ro'yxat ichidagi 
har bir elementni alohida qatordan konsolga chiqarish, yoki bo'lmasa 
har bir elementni kvdartaga oshirish va hokazo. 
Mana shunday vaziyatlarda bizga 
for
operatori yordam beradi. Dasturlashda bu tsikl (loop) deb ataladi. 
Keling quyidagi misolni ko'ramiz. Bizda mehmonlar ro'yxati bor, 
biz har bir mehmonning ismini yangi qatordan chiqarmoqchimiz. 
Buning uchun quyidagi kodni yozamiz:
"""


# mehmonlar = ["Asomiddin", "Muhammad", "Jamshid", "Sardorbek", "Abdulloh", "Sarvar", "Anvar", "Jabbor"]
# print(f" Assalomu alaykum {mehmonlar[0]}")
#
#
# mehmonlar = ["Asomiddin", "Muhammad", "Jamshid", "Sardorbek", "Abdulloh", "Sarvar", "Anvar", "Jabbor"]
# print(f"Assalomu alaykum {mehmonlar[1]}")
#
# mehmonlar = ["Asomiddin", "Muhammad", "Jamshid", "Sardorbek", "Abdulloh", "Sarvar", "Anvar", "Jabbor"]
# print(f"Assalomu alaykum {mehmonlar[2]}")


# mehmonlar = ["Asomiddin", "Muhammad", "Jamshid", "Sardorbek", "Abdulloh", "Sarvar", "Anvar", "Jabbor"]
# for mehmon in   mehmonlar:
#     print(f"Assalomu alaykum {mehmon}")
#     print(f"Hayr {mehmon}")



### bu tepadagi koddan farqi shundaki 2-print for
###sikldan tashqarida bo'lgani uchn sik tugagandan keyn bir marta ishlaydi

# mehmonlar = ["Asomiddin", "Muhammad", "Jamshid", "Sardorbek", "Abdulloh", "Sarvar", "Anvar", "Jabbor"]
# for mehmon in mehmonlar:
#     print(f"Assalomu alaykum {mehmon}")
# print(f"Hayr {mehmon}")



# mehmonlar = ["Asomiddin", "Muhammad", "Jamshid", "Sardorbek", "Abdulloh", "Sarvar", "Anvar", "Jabbor"]
# for mehmon in mehmonlar:
#     print(f"Assalomu alaykum hurmatli {mehmon} sizni 15-yanvarga nahorga oshga taklif qilamiz!!!")
#     print("Hurmat bilan Abdullayevlar honodoni!!!")


# sonlar=range(1, 20)
# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2} ga teng ")


# kv_sonlar = []
# sonlar = list(range(1, 20))
# for son in sonlar:
#     kv_sonlar.append(son**2)
# print(f"1 dan 20 gacha bo'lgan sonlarning kvadratlari {kv_sonlar} lar orasidan ko'rishingiz mumkun ")



# dostlar = []
# print("Assalomu alaykum 8 ta eng yaqin do'stingizni kiriting !!!")
# for i in range(8):
#     dostlar.append(input(f"{i+1} - oshnagizni kiriting : "))
# print(f"Sizning do'stlaringizning ro'yxati : {dostlar}")


# savat = []
# print("Siz olmoqchi bo'lgan maxsulotlarni ro'yxatni tuzib bering!!! ")
# n=int(input("Nechta maxsulot olmoqchisiz : "))
#
# for i in range( n):
#     savat.append(input(f"{i+1} -  maxsulotni kiriting : "))
#
# print(f"Siz olmoqchi bo'lgan maxsulotlar ro'yxati {savat}")



# Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing,
# va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
# royxat = []
# print(f"Royxatga 5 ta ism qo'shishingiz kerak !!! ")
# for i in range(5):
#     royxat.append(input(f"{i+1} - odamni qo'shing : "))
# for ism in royxat:
#     print(f"Assalomu alaykum {ism} sizni va oila azolaringizni to'yga taklif qilamiz!!!")


# Yuoqirdagi tsikl tugaganidan so'ng,
# ekranga "Kod n marta takrorlandi" degan xabar chiqaring
# (n o'rniga kod necha marta takrorlanganini yozing)
# n=1
# ismlar = ["Abdulla", "Abdulloh", "Alisher", "Sarvar", "Sardor", "Asomiddin"]
# for ism in ismlar:
#     print(f"{ism} - ismi {ismlar.index(ism)+1} - ism ")
# print(f"Siz qaytargan sikl {len(ismlar)} marta takrorlandi!!!")


# 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing.
# Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
# toq_son=[]
# for son in range(9, 100, 2):
#     toq_son.append(son)
# print(f"10 dan 100 gacha bo'lgan sonlar to'plami \n{toq_son}")



# Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang,
# va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
# kinolar = []
# ism = input("Assalomu alaykum ismingizni kiriting : ")
# print(f"{ism} o'zingiz yoqdirgan 5 ta kinoni kiriting !!!")
# for kino in range(0, 5):
#     kinolar.append(input(f"{kino + 1} - kinoni nomini kiriting : "))
# print(f"Siz kiritgan kinolar {len(kinolar)} ta va kinolar nomi quydagilar : \n{kinolar}")




# Foydalanuvchidan bugun nechta odam bilan
# uchrashganini (suhbatlashganini) so'rang,
# va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
# royxat = []
# ism = input("Assalomu alaykum hurmatli foydalanuvchi ismingizni kiriting : ")
# savol = int(input(f"{ism} bugun uchrashgan insonlaringiz sonini kiriting : "))
# for i in range(savol):
#     royxat.append(input(f"{ism} {i+1} - uchrashgan insoningizni ismini kiriting : "))
# print(f"{ism} siz bugun {len(royxat) } ta odam bilan uchrashgansiz va ularning ro'yxatni ko'rishingiz mumkun: \n{royxat}")





for i in range(1, 10):
    print(i)

























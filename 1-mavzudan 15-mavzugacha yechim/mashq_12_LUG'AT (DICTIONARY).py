"""
LUG'AT ELEMENTLARI BILAN ISHLASH

"""


# tel_marka={
#     "asomiddin":"samsung03",
#     'abdulloh':"iphone12",
#     'ali':"redmi10",
#     'sarvar':'redmi12',
#     'abror':'ultra23',
#     'sharofiddin':"hiomi",
#     'sardor':"galaxy 9"
# }
#
# for kalit , qiymat in tel_marka.items():
#     print(f"Kalit: ", kalit)
#     print(f"Qiymat: ", qiymat)



# tel_marka={
#     "asomiddin":"samsung03",
#     'abdulloh':"iphone12",
#     'ali':"redmi10",
#     'sarvar':'redmi12',
#     'abror':'ultra23',
#     'sharofiddin':"hiomi",
#     'sardor':"galaxy 9"
# }
#
# key = tel_marka.keys()
# ism = input(f"Assalomu alaykum bizning talabalarning ro'yxati: \n{list(key)} \ntalabani ismni kiritib uning telfon markasni bilib olsangiz bo'ladi: ").lower()
# if ism in key :
#     print(f"Siz kiritgan {ism.title()} ismli talabamiz {tel_marka[ism]} markali telefon ishlatadi! ")
# else:
#     print(f"Kechirasiz siz kiritgan {ism.title()} ismli talaba ro'yhatdan topilmadi! ")



# mevalar = {
#     'olma':12000,
#     "anor":25000,
#     "olcha":20000,
#     "anjir":30000,
#     "sabzi":5000,
#     "shakar":20000,
#     'non':3000,
#     'tarvuz':25000,
#     "qovun":20000,
#     'roltn':3500
# }
#
# print("Assalomu alaykum bizning do'konda bor maxsulotlar: ")
# for key in mevalar:
#     print(key.title())
# harid = input("Bu maxsulotlardan qay birni harid qilmoqchisiz : ").lower()
# if harid in mevalar:
#     print(f"Siz harid qilgan maxsulot: {harid} va uning narhi: {mevalar[harid]} so'm")
# else:
#     print(f"Siz yozgan maxsulot topilmadi! ")




# mevalar = {
#     'olma':12000,
#     "anor":25000,
#     "olcha":20000,
#     "anjir":30000,
#     "sabzi":5000,
#     "shakar":20000,
#     'non':3000,
#     'tarvuz':25000,
#     "qovun":20000,
#     'roltn':3500
# }
# print("Assalomu alaykum bizda borm maxsulotlarni narxi bilan birga ko'rishingiz mumkun: ")
# for key , velue in mevalar.items():
#     print("Maxsulot nomi: ", key ,"Maxsulot narxi: ", velue, "so'm")
# narh = 0
# maxsulot = []
# savol = int(input("Nechta maxsulot harid qilmoqchisiz: "))
# for surov in range(1, savol+1):
#     harid = input(f"{surov} - maxsulot nomini kiriting: ").lower()
#     if harid in mevalar:
#         maxsulot.append(harid)
#         narh  +=  mevalar[harid]
#     else:
#         print(f"{harid} maxsuloti yo'q!")
# print(f"Siz harid qilgan maxsulotlar: {maxsulot} va ularning jami summasi: {narh} so'm")




# mevalar = {
#     'olma':12000,
#     "anor":25000,
#     "olcha":20000,
#     "anjir":30000,
#     "sabzi":5000,
#     "shakar":20000,
#     'non':3000,
#     'tarvuz':25000,
#     "qovun":20000,
#     'roltn':3500
# }
#
# bozorlik = ['olma', 'somsa', 'anor', 'olcha', 'banan']
# for maxsulot in bozorlik:
#     if maxsulot in mevalar:
#         print(f"Siz olgan maxsulot : {maxsulot}ning narxi : {mevalar[maxsulot]} so'm ")
#     else:
#         print(f"Sizning bozorlik ro'yxatingizdagi {maxsulot} bizda yo'q")


# mevalar = {
#     'olma':12000,
#     "anor":25000,
#     "olcha":20000,
#     "anjir":30000,
#     "sabzi":5000,
#     "shakar":20000,
#     'non':3000,
#     'tarvuz':25000,
#     "qovun":20000,
#     'roltn':3500
# }
# narh = 0
# yoq = []
# bor = []
# olingan = ['olma', 'anor', 'shaftoli', 'qovun', 'tarvuz', 'salat']
# for maxsulot in sorted(mevalar):
#     if maxsulot not in olingan:
#         yoq.append(maxsulot)
#         print(f"Assalomu alaykum {maxsulot.title()} sizlarda qolmabdi iltimos yana olib keling ")
#     else:
#         bor.append(maxsulot)
#         narh += mevalar[maxsulot]
#         print(f"Siz sotib olgan maxsulot : {maxsulot.title()} va uning narxi : {mevalar[maxsulot]} so'm ")
# print(f"Siz olgan jami maxsulotlar : {bor} Siz qilgan haridning jami summasi : {narh} so'm")
# print(f"Sizlarda yo'q yani qolmagan maxsulotlar : {yoq}")


# royhat = []
# print("Assalomu alaykum menga so'z kiritsangiz tartiblab chiqarib beraman  ")
# savol = int( input(f"Bu so'zlarni nechta ekanligni kiriting: "))
# for soz in range(1, savol):
#     royhat.append(input(f"{soz} - so'zni kiriting: "))
# royhat.sort()
# print(royhat)



# mevalar = {
#     'olma':12000,
#     "anor":25000,
#     "olcha":20000,
#     "anjir":30000,
#     "sabzi":5000,
#     "shakar":20000,
#     'non':3000,
#     'tarvuz':25000,
#     "qovun":20000,
#     'roltn':3500
# }
# print(sorted(mevalar))
# surov = input("Assalomu alaykum maxsulot nomini kiriting: ")
# if surov not in mevalar :
#     print(f"Siz so'ragan {surov.title()} qolmagan")
# else:
#     print(f"Siz so'ragan {surov.title()} so'rovi qabul qilindi uning narxi : {mevalar[surov]} so'm")



# tel_marka={
#     "asomiddin":"samsung 03",
#     'abdulloh':"iphone 12",
#     'ali':"redmi 10",
#     'sarvar':'redmi 12',
#     'abror':'ultra 23',
#     'sharofiddin':"hiomi",
#     'sardor':"galaxy 9",
#     'davron': "redmi 12",
#   "Muhammad": "iphon 12" ,
#     "Yusuf": "redmi 10",
#     "Jafar": "redmi 12",
#     "Sadulla":"iphon 12"
# }
#
# print(f"Bizning foydalanuvchilarning telefonlari!")
# for tel in tel_marka.values():
#     tel = tel.title()
#     print(tel)



# tel_marka={
#     "asomiddin":"samsung 03",
#     'abdulloh':"iphone 12",
#     'ali':"redmi 10",
#     'sarvar':'redmi 12',
#     'abror':'ultra 23',
#     'sharofiddin':"hiomi",
#     'sardor':"galaxy 9",
#     'davron': "redmi 12",
#   "Muhammad": "iphon 12" ,
#     "Yusuf": "redmi 10",
#     "Jafar": "redmi 12",
#     "Sadulla":"iphon 12"
# }
# print("Bizning foydalanuvchilarimiz foydalanadigan telfon markalari ")
# for tel in set(tel_marka.values()):  #  Set funksiyasidan foydalandim
#     print(tel.title())




# tel_marka={
#     "asomiddin":"samsung 03",
#     'abdulloh':"iphone 12",
#     'ali':"redmi 10",
#     'Yusuf':'redmi 12',
#     'abror':'ultra 23',
#     'sharofiddin':"hiomi",
#     'sardor':"galaxy 9",
#     'davron': "redmi 12",
#   "Muhammad": "iphon 12" ,
#     "Yusul": "redmi 10",
#     "Jafar": "redmi 12",
#     "Sadulla":"iphon 12"
# }
# st = set(tel_marka.values())
# print(st)


# set_m = {'olma', 'anor', 'olma', 'sharbat', 'anjir', 'olcha', 'anjir', 'shaftoli', 'olma'}
# print(type(set_m))   # set takrorlanishlarga ruxsat bermaydi
# print(set_m)
# set1 = set_m.remove('olma')
# print(set_m)
# set_1 = set_m.pop() # Tasodifiy elementni olib tashlaymiz va uni chiqaramiz
# print(set_1)



 
































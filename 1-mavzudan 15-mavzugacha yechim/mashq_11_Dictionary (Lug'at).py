"""
LUG'AT BILAN TANISHUV

"""

"""
Lug'at, ma'lumotlarni bizga tushunarliroq ko'rinishda 
saqlash imkonini beradi. Misol uchun biz biror avtomobilga 
oid lug'at yaratishimiz va lug'atda shu avtoga tegishli barcha 
ma'lumotlarni saqlashmiz mumkin (nomi, rangi, yili, motori, narhi va hokazo). 
"""


# car = {'modeli' : 'BMW', 'color' : 'Blue', 'len':'3.14'}
# print(car)



# car = {'modeli' : 'BMW', 'color' : 'Blue', 'len':'3.14'}
# print(f"Men olgan mashinaning mdeli : {car['modeli']}")


# car = {'modeli' : 'Gelik', 'color' : 'Blue', 'len':'3.14'}
# print(f"Men yoqdirgan mashina : {car['modeli']}, uning rangi : {car['color']}, uzunligi esa : {car['len']} m ni tashkil qiladi!")


# en_uz = {"color":"rang", "onyon":"piyoz", "tree":"Daraxt", "blue":"ko'k"}
# print(f"Bizda bor inglizcha lug'atlar {en_uz}")
# print(f"Color so'zning tarjimasi : {en_uz['color']}")


# talaba = {"ism":"Asomiddin", 'yoshi':19, "t_yil":2005, "t_joy":"Bandixon", "oqish_joy":"Termiz"}
# print(f"Menning ismim : {talaba['ism']} , Tug'ilgan joyim : {talaba['t_joy']}, Tug'ilgan yilim : {talaba['t_yil']}, Yoshim : {talaba['yoshi']} da , O'qish joyim : {talaba['oqish_joy']}")




#
# talaba = {'ism': 'Anvar', 't_yil':2005, 'yosh':19}
# print(f"Talabaning ismi: {talaba['ism']},\
#  Tug'ilgan yili: {talaba['t_yil']} Yoshi: {talaba['yosh']} da "
#     )
# talaba["kurs"] = 2
# talaba["fakultet"] = 'Axborot texnalogiyalar'
# talaba['oqsh_joy'] = "Termiz"
# print(talaba)
# talaba['ism'] = 'Asomiddin'
# print(talaba)
#
# print(f"""
# Talabaning ismi: {talaba['ism']}, Tug'ilgan yili: {talaba['t_yil'], }
# Yoshi: {talaba['yosh']}, O'qish joyi: {talaba["oqsh_joy"]}, Kursi: {talaba['kurs']},
# Fakulteti: {talaba['fakultet']} da o'qib talim oladi!
# """)


# talaba1={}
# talaba1['ism']="Abdulloh"
# talaba1['yosh']=19
# talaba1["kurs"]=2
# print(talaba1)
# print(f"Assalomu alykum {talaba1['ism']} sizni {talaba1['kurs']} - kurs bo'lgangiz bilan tabriklayman!")
# print(f"Yoshingiz ham {talaba1['yosh']} da bo'lgangiz bilan tabriklayman'")
#
# del talaba1['yosh']
# del talaba1['ism']
# print(talaba1)



# tel_marka={
#     "asomiddin":"samsung03",
#     'abdulloh':"iphone12",
#     'ali':"redmi10",
#     'sarvar':'redmi12',
#     'abror':'ultra23',
#     'sharofiddin':"hiomi",
#     'sardor':"galaxy 9"
#
# }
# print(tel_marka)
# print(f"Bizda bor odamlarning ishlatadigan telfonlarni ko'rshingiz mumkun: \n{tel_marka}")
# ism=input("Assalomu alykum kimning ishlatadigan telfon markasi kerak bo'lsa yozing: ").lower()
# print(tel_marka[ism])




# tel_marka={
#     "asomiddin":"samsung 03",
#     'abdulloh':"iphone 12",
#     'ali':"redmi10",
#     'sarvar':'redmi 12',
#     'abror':'ultra 23',
#     'sharofiddin':"hiomi",
#     'sardor':"galaxy 9"
# }
# print(f"Bizda ishlaydigan bollarning tel markalari:\n{tel_marka} ")
# ism = input("Kimning telfon markasni bilishni istasangiz ismini kiriting: ").lower()
# javob = tel_marka.get(ism, f"Afsuski {ism} ismi ro'yxatda topilmadi!")
# if ism in tel_marka:
#     print(f"Siz so'ragan {ism} ning telfon markasi {javob} ")
# else:
#     print(javob)




# tel_marka={
#     "asomiddin":"samsung03",
#     'abdulloh':"iphone12",
#     'ali':"redmi10",
#     'sarvar':'redmi12',
#     'abror':'ultra23',
#     'sharofiddin':"hiomi",
#     'sardor':"galaxy 9"
# }
# print(tel_marka.items())
# for kalit, qiymat in tel_marka.items():
#     print(f"Foydalanuvchi ismi: ", kalit)
#     print("Foydalanuvchi telfoni: ", qiymat)



# tel_marka={
#     "asomiddin":"samsung03",
#     'abdulloh':"iphone12",
#     'ali':"redmi10",
#     'sarvar':'redmi12',
#     'abror':'ultra23',
#     'sharofiddin':"hiomi",
#     'sardor':"galaxy 9"
# }
# ism = input("Assalomu alaykum kimni telfon markasni bilmoqchi siz ismin kiriting: ").lower()
# if ism in tel_marka:
#     print(f"Siz so'ragan {ism.title()}ning ishlatadigan telfon markasi {tel_marka[ism]} ")
# else:
#     print(f"Afsuski siz so'ragan {ism.title()}ning malumotlari ro'yxatdan topilmadi!")












































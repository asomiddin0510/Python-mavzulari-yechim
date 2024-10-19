"""
NESTING

"""

# car0 = {
#         'model':'lacetti',
#         'rang':'oq',
#         'yil':2018,
#         'narh':13000,
#         'km':50000,
#         'korobka':'avtomat'
#         }
# car1 = {
#     'model':"kaptiva",
#     'rang':'qora',
#     'yil':2020,
#     'narh':20000,
#     'km':100000,
#     'korobka':'mexanik'
# }
# car2 = {
#     'model':"matiz",
#     'rang':'sariq',
#     'yil':2023,
#     'narh':5000,
#     'km':40000,
#     'korobka':'mexanik'
# }
# car3 = {
#     'model':"nexia",
#     'rang':'oq',
#     'yil':2024,
#     'narh':10000,
#     'km':10000,
#     'korobka':'mexanik'
# }
# print("Bizda sotuvga qo'yilgan aftomobillarni ko'rishingiz mumkun!")
# cars = [car0, car1, car2, car3]#  Ro'yhatning ichga lug'atni kiritish
# for car in cars:
#     print(f"{cars.index(car)+1} - aftomobil va uning danlelari: "
#           f"Madeli: {car['model'].title()}, "
#           f"Rangi: {car['rang'].title()}, "
#           f"Yili: {car['narh']} $, "
#           f"Yurgani: {car['km']} km, "
#           f"Karobkasi: {car['korobka'].title()} ")

#
# mashinalar = []
# for mashina in range(8):
#     new_car = {
#         'model':"jentra",
#         'rang':None,
#         'yil':2024,
#         'narh':None,
#         'km':0,
#         'korobka':'mexanik'
#     }
#     mashinalar.append(new_car)
#
#
#
# for mashina in mashinalar[:2]:
#     mashina['rang'] = 'qora'
# print(mashina)
#
#
# for mashina in mashinalar[2:5]:
#     mashina['rang'] = 'oq'
# print(mashina)
#
#
# for mashina in mashinalar[5:9]:
#     mashina['rang'] = 'sariq'
# print(mashina)
#
#
# for mashina in mashinalar[:2]:
#     mashina['narh'] = 20000
#
# for mashina in mashinalar[2:5]:
#     mashina['narh'] = 22000
#
# for mashina in mashinalar[5:9]:
#     mashina['narh'] = 25000
#
# print(f"Bizda bor mashinalar : ")
# for mashina in mashinalar:
#     print(mashina)



# dasturchilar = {
#     'asomiddin':['python', 'sql', 'telegram bot', 'django'],
#     'anvar':['html', 'scc', 'java script', 'bootstrap'],
#     'asliddin':['python', 'telegram bot', 'pster sql'],
#     'hikmat':['html', 'scc', 'java script'],
#     "og'abek":['C++', 'python']
# }
# print("Bizning dasturchi: ")
# for dasturchi , tillar in dasturchilar.items():
#     print(f" {dasturchi.title()}", end=" ")
#     print("ning Biladigan texnalogiyalari:", )
#     for til in tillar:
#         print(f" {til.title()}")


# cars = []
# car_s = int(input("Assalomu alykum nechta afto mobila chiqarmoqchisiz: "))
# model = input("Modelni kiriting: ")
# rang = input("Rangni kiriting: ")
# sanasi = input("Yilni kiritng: ")
# narxi = int(input("Narhni kiriting $ da: "))
# karobka = input("Karobkasini kiriting: ")
# for n in range(1, car_s):
#     car_new = {
#          "model": f"{model}",
#             "rang": f"{rang}",
#         "sanasi": f"{sanasi}",
#         "narhi": f"{narxi}",
#         "kaarobka": f"{karobka}"
#     }
#
#     cars.append(car_new)
# print(cars)

# cars = []
# for n in range(5):
#     new_car = {
#         "model": None,
#         "rang": None,
#         "narx": None,
#         "karobka": "mexanik"
#     }
#     cars.append(new_car)
#
# for car in cars[:2]:
#     car["model"] = "Malibu"
#     car["rang"] = "Qora"
#     car["narx"] = 24000
#
#
# for car in cars[2:4]:
#     car['model'] = 'Nexia'
#     car['rang'] = 'oq'
#     car['narx'] = 16
#
#
# for car in cars[4:6]:
#     car['model'] = 'Jentra'
#     car['rang'] = 'qora'
#     car['narx'] = 18
#
# for car in cars:
#     print(f"{cars.index(car)+1} - mashina : {car['model']} uning malumotlari: \nRangi : {car['rang']}, {car['narx']} ming $ ")



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
# for key in tel_marka.items():
#     print(key)

# for key in tel_marka:
#     print(key, tel_marka[key])



# tel_marka={
#     "asomiddin":["samsung 03", 'iphon 11', 'iphon 16'],
#     'abdulloh':["iphone 12", 'redmi 12', 'samsung 21'],
#     'ali':["redmi 10", 'redmi 12'],
#     'Yusuf':['redmi 12', 'iphon 12'],
#     'abror':['ultra 23', 'iphon 13'],
#     'sharofiddin':["hiomi", 'redmi 8'],
#     'sardor':["galaxy 9", 'samsung 20'],
#     'davron': ["redmi 12", 'redmi 12'],
#   "Muhammad": ["iphon 12", 'iphon 14'] ,
#     "Yusul": ["redmi 10"],
#     "Jafar": ["redmi 12", 'redmi 13'],
#     "Sadulla":["iphon 12", 'samsung 24']
# }
# for key , velue in tel_marka.items():
#     print(f"Foydalanuvchi ismi : {key.title()}")
#     print('Uning ishlatgan telfonlari: ')
#     for qiymat in velue:
#         print(f" {qiymat.title()}")

# tepadagi for siklning ikkinchi turi
# for key , velue in tel_marka.items():
#     print(f"Bizning foydalanuvchilar: ", key.title())
#     print(f"Ularning ishlatgan telfon markalari: ", end = "")
#     print(", ".join(tel.title() for tel in velue))



# mevalar = ['olma', 'anor', 'shaftoli', 'olcha', 'banan', 'qovun', 'tarvuz']
# print(", ".join(mevalar))





# tel_marka={
#     "asomiddin":["samsung 03", 'iphon 11', 'iphon 16'],
#     'abdulloh':["iphone 12", 'redmi 12', 'samsung 21'],
#     'ali':["redmi 10", 'redmi 12'],
#     'Yusuf':['redmi 12', 'iphon 12'],
#     'abror':['ultra 23', 'iphon 13'],
#     'sharofiddin':["hiomi", 'redmi 8'],
#     'sardor':["galaxy 9", 'samsung 20'],
#     'davron': ["redmi 12", 'redmi 12'],
#   "Muhammad": ["iphon 12", 'iphon 14'] ,
#     "Yusul": ["redmi 10"],
#     "Jafar": ["redmi 12", 'redmi 13'],
#     "Sadulla":["iphon 12", 'samsung 24']
# }
# for key , velue in tel_marka.items():
#     print(", ".join(tel.title() for tel in velue))




























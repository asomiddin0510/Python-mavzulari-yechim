
#
# class Talaba :
#     def __init__(self, ism, familya, t_yil) :
#         self.ism = ism
#         self.familya = familya
#         self.t_yil = t_yil
#         self.bosqich = 1
#
#
#
#     def get_name(self) :
#         return self.ism
#
#
#     def get_lastname(self) :
#         return self.familya
#
#
#     def get_year(self, now_year) :
#         return now_year - self.t_yil
#
#
#     def get_bosqich(self) :
#         return self.bosqich
#
#     def set_bosqich(self, yangi_bosqich) :
#         self.bosqich = yangi_bosqich
#
#
#     def update_bosqich(self) :
#         self.bosqich += 1
#
#
#     def get_info(self) :
#         return f"Talaba ismi: {self.ism}, familyasi: {self.familya}, tug'ilgan yili: {self.t_yil}-yil va {self.bosqich}-bosqich talabasi."
#
#
#
# talaba1 = Talaba("Asomiddin", "Abduqahharov", 2005)
# talaba2 = Talaba("Alisher", "Usmonov", 2002)
# talaba3 = Talaba("Samandar", "Abdullayev", 2003)
# talaba4 = Talaba("Abror", "Alimov", 2001)
#
# # print(talaba4.get_info())



#
# class Fan :
#     def __init__(self, nomi) :
#         self.nomi = nomi
#         self.talabalar = []
#         self.talabalar_soni = 0
#
#
#     def add_student(self, talaba) :
#         self.talabalar.append(talaba)
#         self.talabalar_soni += 1
#
#
#     def get_students(self) :
#         return [talaba.get_info() for talaba in self.talabalar]
#
#
#
# def see_methodes(klass) :
#     return [method for method in dir(klass) if method.startswith("__") == False ]
#
# # print(see_methodes(Talaba))
# # print(see_methodes(Fan))
# # print(dir(Fan))
# # print(dir(Talaba))
#
#
#
# matem = Fan("Oliy matematika")
# matem.add_student(talaba1)
# matem.add_student(talaba2)
# matem.add_student(talaba3)
# # print(matem.talabalar_soni)
# # print(matem.talabalar)
# # print(matem.nomi)
# print(matem.get_students())

"""
    Avto degan yangi klass yarating. Unga avtomobillarga doir bo'lgan bir nechta xususiyatlar (model, rang, korobka,
    narh va hokazo) qo'shing. Ayrim xususiyatlarga standart qiymat bering (masalan, kilometer=0)

    Avto ga oid obyektning xususiyatlarini qaytaradigan metodlar yozing

        get_info() metodi avti haqida to'liq ma'lumotni matn ko'rinishida qaytarsin

    Avto ga oid obyektning xususiyatlarini yangilaydigan metodlar yozing.

        update_km() metodi son qabul qilib olib, avtomobilning yurgan kilometrajini yangilab borsin

    Yangi, Avtosalon degan klass yarating va kerakli xususiyatlar bilan to'ldiring (salon nomi, manzili, sotuvdagi avtomobillar va hokazo)

    Avtosalonga yangi avtomobillar qo'shish uchun metod yozing

    Avtosalondagi avtomobillar haqida ma'lumot qaytaruvchi metod yozing

    Yuqoridagi obyektlar va ularga tegishli metodlarni tekshirib ko'ring

    dir() funksyasi va __dict__ metodi yordamida o'zingiz yozgan va Pythondagi turli klass va
    obyektlarning xususiyatlari va metodlarini toping (dir(str), dir(int) va hokazo)


"""



#    Avto degan yangi klass yarating. Unga avtomobillarga doir bo'lgan bir nechta xususiyatlar (model, rang, korobka,
#    narh va hokazo) qo'shing. Ayrim xususiyatlarga standart qiymat bering (masalan, kilometer=0)
#    Avto ga oid obyektning xususiyatlarini qaytaradigan metodlar yozing
#  get_info() metodi avti haqida to'liq ma'lumotni matn ko'rinishida qaytarsin

#Avto ga oid obyektning xususiyatlarini yangilaydigan metodlar yozing.
#    update_km() metodi son qabul qilib olib, avtomobilning yurgan kilometrajini yangilab borsin

#
# class Avto :
#     def __init__(self, model, rang, korobka, narh = 20000, i_yil = 2020, kilometr = 0) :
#         self.model = model
#         self.rang = rang
#         self.korobka = korobka
#         self.narh = narh
#         self.i_yil = i_yil
#         self.kilometr = kilometr
#
#
#
#     def get_name(self) :
#         return self.model
#
#
#     def get_color(self) :
#         return self.rang
#
#
#     def upadate_km(self, yangi_kilometr) :
#         self.kilometr = yangi_kilometr
#
#
#     def update_narx(self, yangi_narx ) :
#         self.narh = yangi_narx
#
#
#
#     def get_info(self) :
#         return f"Avtomobil modeli: {self.model}, narxi: {self.narh}$ ming , rangi: {self.rang}, karobka: {self.korobka}, ishlab chiqarilgan yili {self.i_yil}-yil, yurgan yo'li: {self.kilometr} ming km"
#
# avto1 = Avto("Lasetti", 'oq', 'mexanik', 20, 2024, 0)
# avto2 = Avto("Kobolt", 'oq', 'mexanik', 17, 2024, 0)
#
#
# avto2.upadate_km(30)
# avto2.update_narx(15)
# print(avto2.get_info())
#
#
#
#
#
#
#
#
#
#
#
# #Yangi, Avtosalon degan klass yarating va kerakli xususiyatlar bilan to'ldiring (salon nomi, manzili, sotuvdagi avtomobillar va hokazo)
#
# class AvtoSalon :
#     def __init__(self, salon_nomi, salon_manzili ):
#         self.salon_nomi = salon_nomi
#         self.salon_manzili = salon_manzili
#         self.sotuvda_bor_av = []
#         self.sotilgan_avlar = []
#         self.sotuvdagi_avtolar_soni = 0
#         self.sotilgan_avtolar_soni = 0
#
#
#
#     def get_name(self) :
#         return f"Salon nomi: {self.salon_nomi}"
#
#
#     def get_manzil(self) :
#         return f"Salon manzli: {self.salon_manzili}"
#
#     def get_avto_name(self) :
#         return f"Salon nomi: {self.salon_nomi}, {self.get_avto_name()}"
#
#     def add_avto(self, avto) :
#         self.sotuvda_bor_av.append(avto)
#
#
#     def get_sotuv_b(self) :
#         return [avto for avto in self.sotuvda_bor_av]
#
#
#     def get_sotilgan(self) :
#         return [avto for avto in self.sotilgan_avlar]
#
#
#
#
#
#
#
#
#
#
#
#
# class Manzil :
#     def __init__(self, viloyat, tuman, mahalla, kocha) :
#         self.viloyat = viloyat
#         self.tuman = tuman
#         self.mahalla = mahalla
#         self.kocha = kocha
#         self.avto = None
#
#
#
#     def get_manzil(self, avto) :
#         self.avto = avto
#         return f"{avto.viloyat} viloyati, {avto.tuman} tumani, {avto.mahalla} mahallasi, {avto.kocha} ko'chasi"
#






























class Talaba :
    def __init__(self, ism, familya, t_yil, tolovshakli) :
        self.ism = ism
        self.familya = familya
        self.t_yil = t_yil
        self.tolovshakli = tolovshakli
        self.bosqich = 1


    def get_name(self) :
        return f"Ismi: {self.ism}"


    def get_lastname(self) :
        return f"Familyasi: {self.familya}"


    def get_fullname(self) :
        return self.ism, self.familya


    def get_age(self, hozirgi_yil = 2024) :
        yosh = hozirgi_yil - self.t_yil
        return f"Yoshi: {yosh} da"


    def get_holat(self) :
        return f"To‘lov shakli: {self.tolovshakli}"



    def get_kurs(self) :
        return f"Kursi {self.bosqich}"


    def set_kurs(self, yangi_kurs) :
        self.bosqich = yangi_kurs

    def get_info(self) :
        return f"Talaba malumoti\nIsmi: {self.ism}, \nFamilyasi: {self.familya}, \nTug'ilgan yili: {self.t_yil}, \nYoshi: {self.get_age()} \nTo'lov shakli: {self.tolovshakli}, \nKursi: {self.bosqich}"




talaba1 = Talaba('Asomiddin', 'Abduqahharov', 2005, 'Grant')
talaba2 = Talaba("Abdulloh", "Alimov", 2002, "Grant")
talaba3 = Talaba("Anvar", "Alisherov", 2001, "Grant")
talaba4 = Talaba("Alisher", "Abdulayev", 2004, "Kantrak")


# print(talaba1.__dict__)
# print(talaba2.__dict__)
# print(talaba4.__dict__.values())



# talaba3.set_kurs(3)
# print(talaba3.get_kurs())
# print(talaba1.get_age())
# print(talaba1.get_info())






class Fan:
    def __init__(self, fan_nomi) :
        self.fan_nomi = fan_nomi
        self.talabalar = []
        self.talabalar_soni = 0


    def add_student(self, talaba) :
        self.talabalar.append(talaba)
        self.talabalar_soni += 1


    def get_talabalar_num(self) :
        return self.talabalar_soni



    def get_talabalar(self) :
        return [talaba.get_fullname() for talaba in self.talabalar]




fan1 = Fan("Matematika")
fan2 = Fan("Ona tili")
fan3 = Fan("Fizika")


fan1.add_student(talaba1)
fan1.add_student(talaba2)
fan1.add_student(talaba3)
fan1.add_student(talaba4)
fan2.add_student(talaba2)
fan2.add_student(talaba1)



# print(fan1.talabalar_soni)
# print(fan1.get_talabalar())
# print(fan2.get_talabalar())
# print(fan3.get_talabalar())







"""Dunder methodni chiqaradigan , dunder bo'lmagan va ikkalasi birgalikda chiqarshi ko'ramiz"""
#Dunder va dundersiz ikkalasi birgalikda
# print(dir(Talaba))

# Dunder bo'lganlar


def see_dunder(klass) :
    return [method for method in dir(klass) if method.startswith("__")]
# print(see_dunder(Talaba))

# Dunder bo'lmaganlar
def see_method(klass) :
    return [method for method in dir(klass) if method.startswith("__") == False]
# print(see_method(Talaba))
# print(see_method(talaba1))







"""AMALIYOT

    Avto degan yangi klass yarating. Unga avtomobillarga doir bo'lgan bir nechta xususiyatlar (model, rang, korobka, narh va hokazo) qo'shing. Ayrim xususiyatlarga standart qiymat bering (masalan, kilometer=0)

    Avto ga oid obyektning xususiyatlarini qaytaradigan metodlar yozing

        get_info() metodi avti haqida to'liq ma'lumotni matn ko'rinishida qaytarsin

    Avto ga oid obyektning xususiyatlarini yangilaydigan metodlar yozing.

        update_km() metodi son qabul qilib olib, avtomobilning yurgan kilometrajini yangilab borsin

    Yangi, Avtosalon degan klass yarating va kerakli xususiyatlar bilan to'ldiring (salon nomi, manzili, sotuvdagi avtomobillar va hokazo)

    Avtosalonga yangi avtomobillar qo'shish uchun metod yozing

    Avtosalondagi avtomobillar haqida ma'lumot qaytaruvchi metod yozing

    Yuqoridagi obyektlar va ularga tegishli metodlarni tekshirib ko'ring

    dir() funksyasi va __dict__ metodi yordamida o'zingiz yozgan va Pythondagi turli klass va obyektlarning xususiyatlari va metodlarini toping (dir(str), dir(int) va hokazo)

"""


class Avto :
    def __init__(self, model, rang, karobka, narx, chiq_yil) :
        self.model = model
        self.rang = rang
        self.karobka = karobka
        self.narx = narx
        self.chiq_yil = chiq_yil
        self.yurgan_km = 0


    def get_name(self) :
        return self.model


    def get_narx(self) :
        return self.narx

    def get_year(self) :
        return self.chiq_yil

    def get_info(self) :
        return f"Modeli: {self.model}, rangi: {self.rang}, karobka: {self.karobka}, \nNarx: {self.narx}, chiqgan yili: {self.chiq_yil}, yurgan yo'li: {self.yurgan_km}.\n"


    def upper_km(self, km_kirit) :
        self.yurgan_km = km_kirit


    def set_narx(self, yangi_narx) :
        self.narx = yangi_narx


avto1 = Avto("Gentra", 'qora', 'mexanika', 20000, 2024)
avto2 = Avto("Lacetti", 'oq', 'mexanika', 15000, 2024)
avto3 = Avto("Nexia", 'oq', 'mexanika', 10000, 2023)
avto4 = Avto("Damas", 'kulrang', 'mexanika', 8000, 2024)


avto1.upper_km(20000)
avto1.set_narx(18000)
# print(avto1.get_info())
# print(avto1.get_narx())



class AvtoSalon :
    def __init__(self, nomi, manzil, avto = " ") :
        self.nomi = nomi
        self.manzil = manzil
        self.avto = avto
        self.avtolar = []
        self.avtolar_soni = 0


    def get_sname(self) :
        return self.nomi


    def get_manzil(self) :
        return self.manzil

    def get_sinfo(self) :
        return f"Salon nomi: {self.nomi}, Manzili: {self.manzil}, {self.get_son()}"

    def get_avtolar(self) :
        return f"{self.nomi} salonidagi mashinalar royxati: \n{[avto for avto in self.avtolar]}"

    def get_son(self) :
        return f"{self.nomi} avto salonidagi mashinalar soni: {self.avtolar_soni} ta"

    def add_avto(self, avto) :
        self.avtolar.append(avto.get_name())
        self.avtolar_soni += 1


salon1 = AvtoSalon("Surxon Avto", "Surxandaryo viloyati termiz tumani")


salon1.add_avto(avto1)
salon1.add_avto(avto2)
salon1.add_avto(avto3)
salon1.add_avto(avto4)
# print(salon1.get_avtolar())
# print(salon1.get_sinfo())






def see_metod(klass) :
    return [method for method in dir(klass) if method.startswith("__") == False]
# print(see_metod(avto1))
# print(dir(str))
# print(dir(int))
# print(see_metod(str))
# print(talaba2.__dict__)
# print(Avto.__dict__)












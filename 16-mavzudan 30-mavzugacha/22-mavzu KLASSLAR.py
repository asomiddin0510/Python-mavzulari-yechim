"""
METODLAR

Har bir obyekt uning ustida bajarish mumkin bo'lgan funksiyalar bilan keladi.
Bu funksiyalar obyekt ichida yashirin bo'ladi,
va biz ularga nuqta va funksiya nomi orqali murojat qilishimiz mumkin.
Bunday funksiyalar shu klass (yoki obyektga) tegishli metodlar deyiladi.

"""
from select import select

"""
KLASS YARATISH

Yangi klass yaratish uchun class operatoridan foydalanamiz va klassimizga tushunarli nom beramiz. Esingizda bo'lsin, 
klass bu hali obyekt emas, bu obyekt uchun shablon. Shuning uchun klass yaratishda shu 
klassdagi obyektlar uchun umumiy bo'lgan xususiyatlar va funksiyalarni o'ylashimiz kerak.
"""



#
# class  Talaba :
#     def __init__(self, ism, familya, t_yil) :
#         self.ism = ism
#         self.familya = familya
#         self.t_yil = t_yil
#
#
#     def tanishtir(self) :
#         return f"Ismim {self.ism}, Familyam {self.familya}, Tug'ilgan yilim {self.t_yil} - yil"
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
#     def get_age(self, yil) :
#         return yil - self.t_yil
#
#
# talaba_1 = Talaba("Asomiddin", "Abduqahharov", 2005)
# talaba_2 = Talaba("Alisher", "Alimov", 2001)
#
#
# talaba_3 = Talaba("Abdulloh", "Salimov", 2000)
# talaba_4 = Talaba("Sayid Akbar", "Shamsiddinov", 2002)
#
#
# # print(talaba_2.ism, talaba_2.familya, talaba_2.t_yil)
# # print(talaba_1.ism, talaba_1.familya, talaba_1.t_yil)
#
#
# print(talaba_1.tanishtir())
# print(talaba_3.get_name())
#
# print(talaba_4.get_age(2024))
# print(talaba_2.get_lastname())




# 1-topshriq.
#Web sahifangiz uchun foydalanuvchi (user) klassini tuzing.
# Klassning xususiyatlari sifatida odatda ijtimoiy tarmoqlar talab qiladigan
# ma'lumotlarni kiriting (ism, foydalanuvchi ismi, email, va hokazo)

# class User :
#     def __init__(self, ism, familya, yosh, email, pasword) :
#         self.ism = ism
#         self.familya = familya
#         self.yosh = yosh
#         self.email = email
#         self.pasword = pasword
#
#     def description(self) :
#         pass
#
#
#     def get_name(self) :
#         pass



import hashlib

# 2-topshriq.
#Klassga bir nechta metodlar qo'shing, jumladan get_info() metodi
# foydalanuvchi haqida yig'ilgan ma'lumotlarni chiroyli qilib chiqarsin (masalan:
# "Foydalanuvchi: alijon1994, ismi: Alijon Valiyev, email: alijon1994@gmail.com).

# class User :
#     def __init__(self, ism, user_name, age, pasword, email) :
#         self.ism = ism
#         self.user_name = user_name
#         self.age = age
#         self.pasword = pasword
#         self.email = email
#
#
#     def get_info(self) :
#         return f"Ismi: {self.ism}, Foydalanuvchi nomi: {self.user_name}, Yoshi : {self.age}, Paroli : {self.pasword}, Pochta: {self.email}"
#
#
#     def get_name(self) :
#         return f"Foydalanuvchi ismi : {self.ism}"
#
#
#     def get_username(self) :
#         return f"Foydalanuvchi nomi :  {self.user_name}"
#
#
#     def get_age(self) :
#         return f"Foydalanuvchi yoshi : {self.age}"
#
#     def get_pasword(self) :
#         return f"Paroli :  {self.pasword}"
#
#     def get_email(self) :
#         return f"Pochta : {self.email}"
#
#
#
#
# foydalanuvchi1 = User('Asomiddin', 'backend_19', 19, 'pasword', 'email.com')
#
# print(foydalanuvchi1.get_info())
# print(foydalanuvchi1.get_email())
# print(foydalanuvchi1.get_username())




# 3-topshriq.
#Klassdan bir nechta obyektlar yarating va uning xususiyatlari va metodlariga murojat qiling.
# class Abutrent :
#     def __init__(self, ism, yosh, curs_fani, curs_narxi) :
#         self.ism = ism
#         self.yosh = yosh
#         self.curs_narxi = curs_narxi
#         self.curs_fani = curs_fani
#
#     def get_info(self) :
#         return f"Abuturent ismi {self.ism}, Yoshi : {self.yosh}, Kursi fani nomi : {self.curs_fani}, Kurs narxi : {self.curs_narxi}"
#
#
#     def get_name(self) :
#         return f"Ismi : {self.ism}"
#
#
#     def get_age(self) :
#         return f"Yoshi : {self.yosh}"
#
#
#     def get_fan(self) :
#         return f"Kurs fan nomi : {self.curs_fani}"
#
#
# oquvchi1 = Abutrent("Alisher", 16, "Huquq", 200000)
# oquvchi2 = Abutrent("Abu Bakr", 17, "Matematika", 350000)
# oquvchi3 = Abutrent("Hasan", 18, "Geografiya", 300000)
#
#
#
# # xususiyatlariga murojat
# print(oquvchi1.ism)
# print(oquvchi2.ism)
# print(oquvchi3.ism)
# print(oquvchi1.yosh)
# print(oquvchi2.yosh)
# print(oquvchi3.yosh)
#
#
#
# # metodlariga murojat
# print(oquvchi2.get_info())
# print(oquvchi2.get_name())
# print(oquvchi3.get_info())
# print(oquvchi1.get_info())



# class Kitob :
#     def __init__(self, nomi, raqami, turi) :
#         self.nomi = nomi
#         self.raqami = raqami
#         self.turi = turi
#
#     def get_name(self) :
#         return self.nomi
#
#
#     def get_number(self) :
#         return self.raqami
#
#
#     def get_type(self) :
#         return self.turi
#
#
#
#     def get_info(self) :
#         return f"Kitob nomi: {self.nomi}, tartib raqami: {self.get_number()}, turi: {self.get_type()}"
#
#
#
#
#
# kitob1 = Kitob("O'tgan kunlar", 1, "Roman")
# kitob2 = Kitob("Ikki eshik orasi", 2, "Dramma")
# kitob3 = Kitob("Tasavuf haqida", 3, "Tasavuf haqida")
#
# print(kitob1.get_number())
# print(kitob1.get_info())




class Talaba :
    def __init__(self, ism, familya, t_yil) :
        self.ism = ism
        self.familya = familya
        self.t_yil = t_yil
        self.yosh = None


    def get_name(self) :
        return f"Ismi: {self.ism}"


    def get_lastname(self) :
        return f"Familyasi: {self.familya}"


    def get_age(self, hozirgi_yil) :
        self.yosh = hozirgi_yil - self.t_yil
        return f"Yoshi: {self.yosh}"


    def get_info(self) :
        return f"Ismi: {self.ism}, familyasi: {self.familya}, yoshi: {self.yosh}"





talaba1 = Talaba("Sherxon", "Usmonov", 2002)
talaba2 = Talaba("Xusniddin", "Keldiyev", 2001)
talaba3 = Talaba("Eldor", "Sanjarov", 2003)
talaba4 = Talaba("Usmon", 'Umarov', 1999)


print(talaba1.ism, talaba1.familya, talaba1.t_yil)
print(talaba2.get_age(2024))
print(talaba2.get_info())
talaba3.get_age(2024)
print(talaba3.get_info())





"""    Web sahifangiz uchun foydalanuvchi (user) klassini tuzing. Klassning xususiyatlari sifatida odatda ijtimoiy tarmoqlar talab qiladigan ma'lumotlarni kiriting (ism, foydalanuvchi ismi, email, va hokazo)

    Klassga bir nechta metodlar qo'shing, jumladan get_info() metodi foydalanuvchi haqida yig'ilgan ma'lumotlarni chiroyli qilib chiqarsin (masalan: "Foydalanuvchi: alijon1994, ismi: Alijon Valiyev, email: alijon1994@gmail.com).

    Klassdan bir nechta obyektlar yarating va uning xususiyatlari va metodlariga murojat qiling."""

class User :
    def __init__(self, name, user_name, email, new_password, email_password) :
        self.email_password = email_password
        self.name = name
        self.user_name = user_name
        self.email = email
        self.new_password = new_password
        self.agin_password = email_password


    def get_name(self) :
        return f"Name : {self.name}"


    def get_user(self) :
        return f"User name : {self.user_name}"


    def get_email(self, emailpassword) :
        if emailpassword == self.email_password:
            return f"Email : {self.email}"
        else:
            return "Password xato!"

    def get_info(self, password):
        if self.new_password == password :
            return f"Name: {self.name}, user name: {self.user_name}, email: {self.email}, password: {self.new_password}, emil password: {self.email_password}"
        else:
            return f"Password xato!"



user1 = User("Asomiddin", "backend_19", "email@gmil.com", 'asom', 'asom')
user2 = User("Abdulloh", "Alimov", 'emil@gmail.com', 'abd', 'abdulloh')

print(user2.get_info("abd"))
print(user1.get_name())
print(user1.get_info('asom'))

































































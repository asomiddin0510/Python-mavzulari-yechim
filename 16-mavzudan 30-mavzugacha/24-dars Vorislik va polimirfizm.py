
#
# class Shaxs:
#     def __init__(self, ism, familya, passport, t_yil) :
#         self.ism = ism
#         self.familya = familya
#         self.passport = passport
#         self.t_yil = t_yil
#
#
#
#     def get_name(self):
#         return self.ism
#
#
#     def get_fullname(self) :
#         return self.ism, self.familya
#
#     def get_info(self) :
#         return f"Ismi: {self.ism}, familyasi: {self.familya}, passport raqami: {self.passport}, tug'ilgan yili: {self.t_yil}"
#
#
# # inson1 = Shaxs("Asomiddin", "Abduqahharov", 'PS122343', 2005)
# #
# # print(inson1.get_info())
#
#
#
#
# class Manzil:
#     def __init__(self, viloyat, tuman, kocha, uy_raqam) :
#         self.viloyat = viloyat
#         self.tuman = tuman
#         self.kocha = kocha
#         self.uy_raqam = uy_raqam
#     def get_manzil(self) :
#         return f"{self.viloyat} viloyati, {self.tuman} tumani, {self.kocha} ko'chasi, {self.uy_raqam}-uy. "
#
#
#
#
# class Talaba(Shaxs) :
#     def __init__(self, ism, familya, passport, t_yil, idraqam, manzil) :
#         super().__init__(ism, familya, passport, t_yil)
#         self.idraqam = idraqam
#         self.manzil = manzil
#         self.bosqaich = 1
#
#
#     def get_idraqam(self) :
#         return self.idraqam
#
#
#     def get_bosqaich(self) :
#         return self.bosqich
#
#
#     def get_info(self) :
#         result = f"Talabaning ismi: {self.ism}, familyasi: {self.familya}, Passport normeri: {self.passport}, ID raqami: {self.idraqam}"
#         result += f"\nManzil: {self.manzil.get_manzil()}"
#         return result
#
#
#
#
# talaba1_manzil = Manzil("Surxandaryo", 'Bandixon', 'Yangi ariq', 43)
# # print(talaba1_manzil.get_manzil())
# talaba1 = Talaba("Asomiddin", "Abduqahharov", "PS94230394", 2005, "ID243554", talaba1_manzil)
# print(talaba1.get_info())




"""
    Talaba klassiga yana bir, fanlar degan xususiyat qo'shing. Bu xususiyat parametr sifatida uzatilmasin va obyekt yaratilganida bo'sh ro'yxatdan iborat bo'lsin (self.fanlar=[])

    Fan degan yangi klass yarating va bu klassdan turli fanlar uchun alohida obyektlar yarating.

    Talaba klassiga fanga_yozil() degan yangi metod yozing. Bu metod parametr sifatida Fan klassiga tegishli obyektlarni qabul qilib olsin va talabaning fanlar ro'yxatiga qo'shib qo'ysin.

    Talabaning fanlari ro'yxatidan biror fanni o'chirib tashlash uchun remove_fan() metodini yozing. Agar bu metodga ro'yxatda yo'q fan uzatilsa "Siz bu fanga yozilmagansiz" xabarini qaytarsin.

    Yuqoridagi Shaxs klassidan boshqa turli voris klasslar yaratib ko'ring (masalan Professor, Foydalanuvchi, Sotuvchi, Mijoz va hokazo)

    Har bir klassga o'ziga hoz xususiyatlar va metodlar yuklang.

    Barcha yangi klasslar uchun get_info() metodini qayta yozib chiqing.

    Voris klasslardan yana boshqa voris klass yaratib ko'ring. Misol uchun Foydalanuvchi klassidan Admin klassini yarating. 

    Admin klassiga foydalanuvchida yo'q yangi metodlar yozing, masalan, ban_user() metodi konsolga "Foydalanuvchi bloklandi" degan matn chiqarsin.
"""

class Manzil :
    def __init__(self, viloyat, tuman, kocha, uy_raqam) :
        self.viloyat = viloyat
        self.tuman = tuman
        self.kocha = kocha
        self.uy_raqam = uy_raqam



    def get_manzil(self) :
        return f"{self.viloyat} viloyati, {self.tuman} tumani, {self.kocha} ko'chasi, {self.uy_raqam}-uy"


talaba1_manzil = Manzil("Toshkent", "Chirchiq", "Ko'kcha", 23)
talaba2_manzil = Manzil("Surxondaryo", "Termiz", "Istomina", 34)



class Talaba:
    def __init__(self, ism, familya, passport, manzil) :
        self.ism = ism
        self.familya = familya
        self.passport = passport
        self.manzil = manzil
        self.bosqich = 1
        self.fanlar = []
        self.fanlar_son = 0

    def fanga_yozil(self, fan) :
        if fan not in self.fanlar :
            self.fanlar.append(fan)
            self.fanlar_son += 1
            return f"Bu fanga mofaqyatli yozildingiz!"
        else :
            return "Bu fanga oldin ham yozilgansiz!"

    def remove_fan(self, fan) :
        if fan in self.fanlar :
            self.fanlar.remove(fan)
            self.fanlar_son -= 1
            return "Kiritgan fanigiz mofaqyatli o'chrildi!"
        else :
            return "Kiritgan fangiz ro'yxatda yo'q!"


    def get_fanalar(self) :
        return [fan.get_fan() for fan in self.fanlar]


    def fanlarni_ciqar(self) :
        return f"Siz yozilgan fanlar ro'yxati: {self.fanlar} \nFanlar soni: {self.fanlar_son} ta"


    def get_info(self) :
        return (f"Talaba haqida malumotlar: \nIsmi: {self.ism}, familyasi: {self.familya}, Passport raqami: {self.passport}."
                f"\nYashash manzli: {self.manzil.get_manzil()},  yozilgan fanlari soni: {self.fanlar_son} ta."
                f"\nYozilgan fanlari: {self.get_fanalar()}")


talaba1 = Talaba("Alisher", 'Aliqulov', 'PS123535', talaba1_manzil)
talaba2 = Talaba("Abdulloh", "Sadullayev", "PS31435", talaba2_manzil)


# print(talaba1.get_info())

class Fan :
    def __init__(self, fan_nomi) :
        self.fan_nomi = fan_nomi

    def get_fan(self) :
        return self.fan_nomi

fan1 = Fan("Matematika")
fan2 = Fan("Ona tili")
fan3 = Fan("Adabiyot")
fan4 = Fan("Huquq")
fan5 = Fan("Tatrix")
fan6 = Fan("Geografiya")




talaba1.fanga_yozil(fan1)
talaba1.fanga_yozil(fan2)
talaba1.fanga_yozil(fan3)
talaba1.fanga_yozil(fan4)
print(talaba2.get_info())

















































class Shaxs :
    def __init__(self, ism, familya, t_yil, passport ) :
        self.ism = ism
        self.familya = familya
        self.t_yil = t_yil
        self.passport = passport
        self.yosh = None


    def get_name(self) :
        return f"Ismi: {self.ism}"


    def get_lastname(self) :
        return f"Familyasi: {self.familya}"

    def get_age(self, hozirgiyil = 2024) :
        self.yosh = hozirgiyil - self.t_yil
        return f"Yoshi: {self.yosh} da"


    def get_info(self) :
        return f"{self.get_name()}, {self.get_lastname()}\nPassport: {self.passport}, tug'ilgan yili: {self.t_yil}, yoshi: {self.yosh}"








class Manzil :
    def __init__(self, uy, kocha, tuman, viloyat) :
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat


    def get_manzil(self) :
        return f"{self.viloyat} viloyati, {self.tuman} tumani, {self.kocha} ko'chasi, {self.uy}-uy"







class Talaba(Shaxs) :
    def __init__(self, ism, familya, passport, idraqam, t_yil, manzil) :
        super().__init__( ism, familya, t_yil, passport)
        self.idraqam = idraqam
        self.manzil = manzil
        self.bosqich = 1


    def get_id(self) :
        return f"Talaba ID raqami: {self.idraqam}"


    def get_bosqich(self) :
        return f"Talaba bosqichi: {self.bosqich}"


    def get_info(self) :
        return f"{self.ism}, {self.familya}, ID raqam: {self.idraqam}, Passport: {self.passport}, Talaba manzili: {self.manzil.get_manzil()}"




talaba1_manzil = Manzil(43, 'Yangi ariq', 'Bandixon', 'Surxondaryo')
talaba1 = Talaba("Abdulla", 'Baxtiyarov', 'DS1322904DF', "AD124325", 2002, talaba1_manzil)
print(talaba1.get_info())
print(talaba1_manzil.get_manzil())





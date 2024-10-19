"""
#11 BIR NECHTA SHARTLARNI TEKSHIRISH
if-elif-else zanjiri, "and", "or" operatorlari bilan tanishamiz

"""



# savol = int(input("Assalomu alaykum yoshingizni kiriting : "))
# if savol<=10:
#     narh = 5000
# elif savol<=18:
#     narh = 10000
# else:
#     narh = 15000
# print(f"Siz uchun kirish {narh} so'm")


# savol = input("Assalomu alaykum kunni kiriting : ")
# if savol.lower()=="yakshanba" or savol.lower()=='shanba':
#     print(f"Bugun kun {savol} kuni va bugun dam olish kuni!")
# else:
#     print(f"Bugun kun {savol} kuni ish kuni!")


# kun = input("Assalomu alaykum bugun kun nima : ")
# havo = int(input("Bugumgi havo haroratni kiriting :"))
# if (kun.lower()=="yakshanba" or kun.lower()=="shanba") and 10< havo < 30 :
#     print("Bugun havo juda ajoyib dam olishga Tog'ga chiqamiz!!!")
# elif -5<havo<-1:
#     print("Bugun havo juda sovuq shu sababli uyda qolamiz!!!")
# elif -6< havo>30:
#     print("Bugun havo juda no qulayligi sababli ishga bora olmaymiz!!! ")
# else:
#     print("Bugun ishga boramiz!!!")

## Bool malumot turi
# kun = "shanba"
# print(kun=='shanba')


# kun = "yakshanba"
# print(type(kun == 'yakshanba'))

# narh = 10000
# salat = True
# choy = True
# if choy and salat:
#     narh+=10000
# elif choy or salat:
#     narh+=5000
# print(f"Siz sotib olgan narsala narxi {narh} so'm !")



# savol = input("Assalomu alaykum ismningizni kiriting : ")
# yosh = int(input(f"{savol.title()} iltimos yoshindizni kiriting : "))
# if savol.lower()=="sarvar" and yosh ==19:
#     print(f"{savol.title()} siz uchun parkimiz tekin kirishingiz mumkun! ")



# narh = 10000
# non = True
# salat = True
# olma = False
# choy = True
# kalbasa = False
# olcha = True
# xolva = False
# savat = []
# if non:
#     narh += 3000
#     print(f"Siz non oldingiz! ")
# if olma:
#     narh+=8000
#     print("Siz olma oldingiz! ")
# if salat:
#     narh+=15000
#     print("Siz salat oldingiz! ")
# if choy :
#     narh+=5000
#     print("Siz choy sotib oldingiz! ")
# if kalbasa:
#     narh+=40000
#     print("Siz kalabasa oldingiz! ")
# if olcha:
#     narh+=22000
#     print("Siz olcha oldingiz! ")
# if xolva :
#     narh+=20000
#     print("Siz xolva oldingiz! ")
#
# print(f"Siz sotib olgan maxsulotlar narhi {narh} so'm")


# menu = ['somsa', 'kabob', 'shashlik', 'osh', 'norin', 'besh barmoq', 'salat', "lag'mon", "qazi"]
# savol = input("Assalomu alaykum hurmatli mijoz \nNima zakas qiloqchi siz: ")
# if savol.lower() in menu:
#     print(f"Sizning buyurtmangiz qabul qilindi! ")
# else:
#     print(f"Afsuski sizning buyurtmangiz bizda yo'q")





# menu = ['somsa', 'kabob', 'shashlik', 'osh', 'norin', 'besh barmoq', 'salat', "lag'mon", "qazi"]
# savol = input("Assalomu alaykum hurmatli mijoz! \nBizning oshxonamizga hush kelibsiz!\nOvqat buyurtma berishni istaysizmi unda ha yozvuni kiriting:  ")
# if savol.lower()=='ha':
#     savol1=input("Bizdan foydalanmoqchi bo'lganigiz uchun raxmat !\nMenuni ko'rishini istasangiz >>> menu >>> so'zni kiriting : ")
#     if savol1.lower()=='menu':
#         print(f"Bizda bor maxsulotlar : {menu} shulardan iborat ")
#         savol3 = input("Yuqoridagilardan birini tanlang va kiriting :")
#         if savol3.lower() in menu:
#             print(f"Hurmatli mijoz siz {savol3.title()} ni tanladingiz \nTanlovingiz uchun raxmat ")
#         else:
#             print(f"Hurmatli mijoz siz kiritgan {savol3.title()} afsuski bizda yo'q!")
#     else:
#         savol2=input("Menudan ovqat tanlashni istasangiz >>> menu >>> so'zni kiritishingizni so'raymiz : ")
#         if savol2.lower()=="menu":
#             print(f"Bizda bor maxsulotlar : {menu} shulardan iborat  ")
#             savol3 = input("Yuqoridagilardan birini tanlang va kiriting :")
#             if savol3.lower() in menu:
#                 print(f"Hurmatli mijoz siz {savol3.title()} ni tanladingiz \nTanlovingiz uchun raxmat ")
#             else:
#                 print(f"Hurmatli mijoz siz kiritgan {savol3.title()} afsuski bizda yo'q!")
#         else:
#             print("Hurmatli mijoz ilova yoplmoqda! ")
# else:
#     savol4 = input("Hurmatli mijoz buyurtma berishi tugatshni istaysizmi unda >>> tugatish >>> so'zni kiriting : ")
#     if savol4.lower() =="tugatish" :
#         print("Buyurtma berish tugatildi! ")
#     else:
#         print("!!!")





# royhat_gr = ['jalol', 'abdulloh', 'olim', 'kamoliddin', 'abbos', 'sarvar', 'shavkat', 'asomiddin', 'anvar']
# royhat = ['salm', 'sabriddin', 'abdulla', 'alouddin', 'shamsiddin', 'salohiddin', 'muhammad yusuf', 'muhammad karim', 'odil']
#
# yosh=int(input("Assalomu alykum ishtirokchi \nIltimos yoshingizni kiriting: "))
# if 19<=yosh<=26:
#     ism=input("Hurmatli mijoz ismingizni kiriting : ").lower()
#     if ism in royhat_gr:
#         print(f"Tabriklayman {ism.title()} siz {royhat_gr.index(ism)+1} - o'quv grandni qo'lga kiritdingiz ! ")
#     elif ism in royhat:
#         print(f"Tabriklayman {ism.title()} siz {royhat.index(ism)+1 + len(royhat_gr)} - o'quv kontraktni qo'lga kiritdingiz !" )
#     else:
#         print(f"Afsuski {ism.title()} siz ro'yhatdan chiqmadingiz! ")
# else:
#     print("Hurmatli foydalanuvchi siz 19 va 26 yosh oralig'ida bo'lishingiz kerak ")

# jarima_royhat = ['salm', 'sabriddin', 'abdulla', 'alouddin', 'shamsiddin', 'salohiddin', 'komil', 'donyor', 'farhod']
# ism = input("Assalomu alaykum ismingizni kiriting: ").lower()
# if ism not in jarima_royhat:
#     print(f"Tabriklayman {ism.title()} sizning jarimangiz yo'q ekan ")
# else:
#     print(f"Afsuski {ism.title()} sizning jarimangiz bor ")




# bor = []
# menu = ['osh', 'manti', 'somsa', 'kabob', 'cola', 'fanta', 'pepsi', 'senvich', 'holva', 'non', "go'sht", 'norin']
# buyurtma = ['osh', 'manti', 'kabob', 'senvich', 'lola']
# for buyr in buyurtma:
#     if buyr in menu:
#         bor.append(buyr)
#         print(f"Sizning buyurtmangiz {buyr} menuning ichda bor ")
#     else:
#         print(f"Siz kiritgan {buyr} bizning menuda yo'q ")
# print(f"Sizning jami buyurtmangiz {bor} lar ")





# menu = ['osh', 'manti', 'somsa', 'kabob', 'cola', 'fanta', 'pepsi', 'senvich', 'holva', 'non', "go'sht", 'norin']
# buyurtma = []
# ism = input("Assalomu alykum ismngizni kiriting: ")
# sorov = input(f"{ism.title()} menu dan foydalanishni istaysizmi ha yoki yo'q so'zlarni yozishingizni so'raymiz : ")
# if sorov.lower() == 'ha':
#         n = input(f"{ism.title()} menuni ko'rishingiz mumkin : {menu}\nMenudagi elementlarning ichdan nechtasni olmoqchisiz: ")
#         n = int(n)
#         for buyurt in range(n):
#             buyurtma.append(input(f"{ism.title()} menudagi maxsulotlardan tanlang va {buyurt+1} - elementni kiriting: "))
#         savat = input(f"{ism.title()} siz tanlagan maxsulotlar {buyurtma} shulardan iborat\nInter tugmsani bosing! ")
#         if buyurt not in buyurtma:
#             print(f"Siz tanlagan maxsulotlarning hammasi ham menuning ichda yo'q ")
#         else:
#             print("Buyurtmangiz qabul qilindi! ")
# elif sorov.lower() =="yo'q":
#     print(f"{ism.title()} buyurtmangiz yakunlandi! ")




# menu = ['osh', 'manti', 'somsa', 'kabob', 'cola', 'fanta', 'pepsi', 'senvich', 'holva', 'non', "go'sht", 'norin']
# buyrutmalar = ['olma', 'lola', 'shovla']
# if buyrutmalar:
#     print(f"Siznig buyurtmalaringiz soni {len(buyrutmalar)} ta ")
# else:
#     print("Bu ro'yhat bo'sh! ")

























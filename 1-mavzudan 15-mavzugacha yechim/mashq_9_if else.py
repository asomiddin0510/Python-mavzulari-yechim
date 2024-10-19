"""
if OPERATORI

Ushbu darsimizda biz
if
 operatori yordamida shunday shartlarni yozishni, tekshirishni va
 tekshiruv natijasiga ko'ra kodning turli qismlarini bajarishni o'rganamiz.
"""




# mevalar = ['olma', 'shaftoli', 'bexi', 'apilsin', 'banan', 'limon']
# for meva in mevalar:
#     print(f"Men olgan meva : {meva}")


# mevalar = ['olma', 'shaftoli', 'bexi', 'apilsin', 'banan', 'limon']
# for meva in mevalar:
#     if meva=='shaftoli':
#         print(f"{meva.upper()}")
#     else:
#         print(f"{meva.title()}")


# ism = "Asomiddin"
# print(f"Asomiddin tengmi ism degan o'zgaruvchiga >>>", ism=='Asomiddin')


# ism = "Abdulloh"
# print("Abdulloh tengmi ism degan o'zgaruvchiga >>>" , ism=='Asomiddin')


# ism = "ASOMIDDIN"
# print(ism.lower()=='asomiddin')


# ism = input("Assalomu alaykum hurmatli foydalanuvchi iltimos ismingizni kiriting :\n")
# if ism.lower()!="abdulloh":
#     print(f"Hurmatli {ism} bizga Abdulloh kerak ")
# else:
#     print("Tabriklaymiz Abdulloh sizni kutgandik ")


# savol = float(input("Assalomu alaykum hurmatli foydalanuvchi ifodani javobni kiriting 4*15+3 = "))
# if savol!=63:
#     print(f"Javob natog'ri!")
# else:
#     print("Javob to'g'ri!")


# ism= input("Assalomu alaykum ismingizni kiriting : ")
# yosh = int(input(f"Raxmat {ism.title()} tanishganimdan  hursandman \n{ism.title()} yoshingizni kiriting: "))
# if yosh>=18:
#     print(f"{ism.title()} kirishingiz mumkun!")
#     login = input(f"{ism.title()} login kiriting : ")
#     if len(login)>=5:
#         print('Kiritgan logingiz qabul qilindi!')
#     else:
#         print(f"Hurmatli {ism.title()} kiritgan logingiz 5 ta belgidan kam bo'lmasligi kerak! ")
#         login = input(f"{ism.title()} Qaytadan login kiriting : ")
# else:
#     print(f"Hurmatli {ism.title()} yoshingiz 18 dan kichik afsuski kira olmaysiz!")


# ism = input("Assalomu alaykum ismingzni kiriting : ")
# yosh=2024-int(input(f"{ism.title()} tug'lgan yilingizni kiriting : "))
# if yosh>=60 :
#     print(f"{ism.title()} Sizning yoshingiz {yosh} da va siz qariyalar safiga kirasiz!")
# elif yosh>=18 :
#     print(f"{ism.title()} Sizning yoshingiz {yosh} da va o'rta yoshdaglar safiga kirasiz!")
# else:
#     print(f"{ism.title()} Sizning yoshingiz {yosh} da va siz yoshlar safiga kirasiz!")


# son1 = int(input("Assalomu alaykum son kiriting : "))
# son2 = int(input("Yana son kiritibng : "))
# if son1>son2: print(f"Siz kiritgan sonlarning ichda kattasi {son1}")
# else:print(f"Siz kiritgan sonlardan kichigi {son1}")


# a, b=122, 34
# print(a, 'katta', b ,'dan') if a>b else print(a, 'kichik', b, 'dan')




#Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat elementlarining birinchi
# harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car.lower()=='gm':
#         print(car.upper())
#     else:
#         car.title()
#     print(car)



#Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring.
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car.lower()!='gm':
#         print(car.title())
#     else:
#         print(car.upper())



#Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin.
# Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring.
# Aks xolda, "Xush kelibsiz, {foydalanuvchi_ismi}!" matnini konsolga chiqaring.
# ism = input("Assalomu alaykum ismingizni kirting : ")
# login = input(f"{ism.title()} login kiriting : ")
# if login.title()=='Admin':
#     print(f"Xush kelibsiz! {ism.title()} Foydalanuvchilar ro'yxatni ko'rasizmi ?")
# else:
#     print(f"Xush kelibsiz! {ism.title()} ")





#Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa,
# "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
# son1 = int(input("Son kiriting : "))
# son2 = int(input("Yana son kiriting : "))
# if son1==son2:
#     print(son2 , ' teng ' , son2)
# else:
#     print(son2 , ' teng emas ', son1, 'ga')




#Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son",
# agar musbat bo'lsa "Musbat son" degan xabarni chiqaring.
# son1 = int(input("Assalomu alaykum son kiriting : "))
# if son1<0:
#     print(son1, 'manfiy son')
# else:
#     print(son1, 'musbat son')



#Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring.
# Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring.
# son = int(input("Assalomu alaykum son kiriting: "))
# if son>0:
#     print(f"Siz kiritgan {son} ning ildizi {son**0.5} ga teng ")
# else:
#     print('Musbat son kiriting ')































































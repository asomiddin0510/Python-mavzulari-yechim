"""
WHILE, RO'YXATLAR VA LUG'ATLAR
WHILE YORDAMIDA RO'YXATNI TO'LDIRISH

"""


# print("Men kvadrat qaytaraman")  # toki exit ga teng bo'lmaguncha takrorlanadi qachonki exitga teng bo'lguncha takrorlan
# savol = "Istalgan son kiriting dasturni to'xtatish uchun 'exit' yozing : "
# qiymat = " "
# while qiymat != "exit":
#     qiymat = input(savol)
#     if qiymat.lower() != 'exit':
#         print(f"Siz kiritgan {qiymat} ning kvadrati {int(qiymat)**2} ga teng ")
# print("Dastur tugadi !")


# print("Menga son kiriting va sonning kvadratini oling ")
# savol = "Istalgan sonni kiriting yoki to'xtatush uchun (to'xtat) buyrug'ni kiriting : "
# qiymat = " "
# shart = True
# while shart:
#     qiymat = input(savol)
#     if qiymat.lower() == "to'xtat":
#         shart = False
#     else:
#         print(f"Siz kiritgan {qiymat} ning kvadrati {int(qiymat)**2} ga teng ")
# print("Dastur yakunlandi! ")




# print("Menga son kiriting va sonning kvadratini oling ")
# savol = "Istalgan sonni kiriting yoki to'xtatush uchun (stop) buyrug'ni kiriting : "
# qiymat = " "
# while True:
#     qiymat = input(savol)
#     if qiymat.lower() =="stop":
#         break
#     else:
#         print(f"Siz kiritgan {qiymat} ning kvadrati {int(qiymat)**2} ga teng ")
# print("Dastur yakunlandi ")



# for son in range(0, 30):
#     if son == 20:
#         break
#     print(f"{index(son)+1}-son: {son}")



# import cProfile
#
# def calculate_squares():
#     for son in range(0, 20):
#         if son == 10 or son == 12:
#             continue  # continue bu shart bajarilganda o'zidan keyingni taylab siklning boshiga o'tib ketadi
#         print(f"{son} ning kvadrati {son**2} ga teng ")
#
# # cProfile yordamida profiling
# cProfile.run('calculate_squares()')




# for son in range(0, 26):
#     if 13<son<21:
#         continue
#     else:
#         print(son)



# son = 0
# while son<30:
#     son += 1
#     if son%2 == 0:
#         continue
#     else:
#         print(f"Toq son: {son}")




# print("Assalomu alaykum siz biz bilan do'stlaringizni ro'yhatni tuzishingiz mumkun !")
# dostlar = []
# n = 0
# while True:
#     savol = input("Ro'yhat tuzishni istaysizmi (ha/yo'q) : ")
#     if savol.lower() == "ha":
#         dost = input(f"{n+1} - do'stingizning ismini kiriting: ")
#         dostlar.append(dost.title())
#     elif savol.lower() == "yo'q":
#         print("Dastur yakunlandi! ")
#         break
#     else:
#         print("Iltimos ha/yo'q kamandasni kiriting!")
#     n += 1
# print(f"Sizning do'stlaringizning ro'yhati : {dostlar}")




# print("Do'stlaringizni ro'yhatni tuzamiz! ")
# n = 1
# dostlar = []
# while True:
#     savol = f"{n} - do'stingizni ismini kiriting: "
#     ism = input(savol)
#     dostlar.append(ism.title())
#     takrorlash = input("Ro'yhatni davom etrishni istaysizmi (ha/yo'q) : ")
#     n += 1
#     if takrorlash.lower() != "ha":
#         print("Dasturni tugatdingiz!")
#         break
# print(f"Do'stlaringizni ro'yhatni ko'rishingiz mumkun : \n{', '.join(dostlar)}")


# print("Do'stlaringizni ismi va bo'yni kiritishingiz mumkun bo'lgan dastur! ")
# dostlar_mal = {}
# ishora = True
# n = 1
# while ishora:
#     ism = input(f"{n} - do'stingizni ismini kiriting : ")
#     boy = int(input(f"{ism.title()}ning bo'yni kiriting (sm)da : " ))
#     dostlar_mal[ism] = boy
#     savol = input("Hurmatli foydalanuvchi do'stlaringizni ism va malumotlarni kiritishda davom etaszmi (ha/yo'q) : ")
#     n += 1
#     if savol.lower() == "yo'q":
#         ishora = False
#         print("Dasturni to'xtadingiz! ")
# print("Do'stlaringizni ro'yhati!")
# for ism , boy in dostlar_mal.items():
#     print(f"Ismi : {ism.title()}, Bo'yi : {boy} (sm) ")




# print("Siz bu dastur orqali talabalarga baho qo'ya olasiz !")
# talabalar = {}
# n = 1
# while True:
#     ism = input(f"{n} - O'quvchining ismini kiriting : ")
#     baho = int(input(f"{ism.title()}ning bahosni qo'ying: "))
#     talabalar[ism] = baho
#     n += 1
#     savol = input("Dasturni to'xtatishni istasangiz (ha/yo'q)ni kiriting: ")
#     if savol.lower() == "yo'q":
#         print("Dastur tugadi!")
#         break
# print("Talabalarning baholari! ")
# n = 1
# for ism, baho in talabalar.items():
#     print(f"{n} - talaba ismi : {ism.title()} , Bahosi : {baho}")
#     n += 1


# print("Bu dastur bilan yiqilgan va o'tgan talabalarni bahosi bilan ko'rishingiz mumkun! ")
# talabalar = {}
# n = 1
# while True:
#     ism = input(f"{n} - talabaning ismini kiriting : ").title()
#     baho = int(input(f"{ism}ning bahosni kiriting : "))
#     talabalar[ism] = baho
#     savol = input("Dasturni davom etshni istaysizmi? (ha/yo'q): ").lower()
#     n += 1
#     if baho<3:
#         talabalar[ism] = "Yiqilgan!"
#     if savol != "ha":
#         print("Dastur to'xtadi! ")
#         break
# print("O'tgan va o'tmagan talabalar ro'yhatni ko'rishingiz mumkun:")
# n = 0
# for ism , baho in talabalar.items():
#     n += 1
#     print(f"{n} - talaba ismi: {ism}, baho: {baho}")































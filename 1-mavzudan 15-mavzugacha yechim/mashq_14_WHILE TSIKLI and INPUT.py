"""
WHILE TSIKLI and YANA input()

"""
# son = 1
# while son<=6:
#     print(son, end=" ")
#     son+=1


# from random import randint
# ishlatil_kod = [2, 5, 8]
# yangi_kod = randint(1, 8)
# n = 0
# while yangi_kod in ishlatil_kod:
#     n+=1
#     yangi_kod = randint(1, 8)
# print(yangi_kod, "Takrorlanishlar soni: ", n)



# print("Assalomu alaykum men istalgan soning kvadratni qaytaruvchi dasturman !")
# savol = "Isatlgan son kiriting yoki dasturni yakunlamoqchi bolsangiz 'tugatish' deb yozing : "
# qiymat = ' '
# while qiymat != 'tugatish':
#     qiymat = input(savol)
#     if qiymat != 'tugatish':
#         print(f"Siz kiritgan {qiymat} ning kvadrati {int(qiymat)**2} ga teng ")
# print("Dastur tugatildi! ")


# print("\nAssalomu alaykum do'stlaringizni ro'yhatni tuzishda men sizga yordam beraman! ")
# savol1 = "\nRo'yhatni tuzishni boshlaysizmi unda do'stingizning ismini kiriting to'xtatishni istasangiz 'exit' deb yozing : "
# savol2 = "\nKeyingi do'stingizni kiriting yoki 'exit' so'zni yozib dasturni yakunlang: "
# dostlar = []
# qiymat = " "
# n=0
# while qiymat != "exit":
#     n += 1
#     if n==1:
#         qiymat = input(savol1)
#         if qiymat != 'exit':
#             dostlar.append(qiymat.title())
#             print(f"\nTabriklayman {qiymat.title()} ro'yhatga mofaqyatli qo'shildi! ")
#
#     elif qiymat != 'exit':
#         qiymat = input(savol2)
#         if qiymat != 'exit':
#             dostlar.append(qiymat.title())
#             print(f"\nTabriklayman {qiymat.title()} ro'yhatga mofaqyatli qo'shildi! ")
# print(f"Dastur yakunlandi! \n Sizning Do'stlar ro'yhatingizda {len(dostlar)} ta do'stingiz bor ular : \n{dostlar}")


# print("Kiritilgan soning n-darajasni qaytaraman qaytaraman !")
# savol = "Istalagan son kiriting yoki 'exit' ni yozish orqali dasturni to'xtating: "
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         n = int(input("Soning darajasni kiriting: "))
#         print(f"Siz kiritgan {qiymat} ning {n}-darajasi {float(qiymat)**n} ga teng")
# print("Siz exit yordamida dasturni yakunladingiz! ")


# print("Ikki sonni yig'indisini qaytaruvchi dastur! ")
# savol = "Foydalanishni hohlaysizmi (ha/yo'q) javobni kiritng: "
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == "yo'q":
#         ishora = False
#     elif qiymat == 'ha':
#         a = int(input("Birinchi qo'shluvchni kiriting: "))
#         b = int(input("Ikkinchi qo'shuluvchni kiriting: "))
#         s = a + b
#         print(f"Siz kiritga {a} va {b} ning yig'indisi {s} ga teng")
# print("Dastur yakunlandi ")





# print("Ikki sonni ayirmasni qaytaruvchi dastur! ")
# savol = "Foydalanishni hohlaysizmi (ha/yo'q) javobni kiritng: "
# while True:
#     qiymat = input(savol)
#     if qiymat.lower() == "yo'q":
#         break
#     elif qiymat.lower() == 'ha':
#         a = int(input("Ayrluvchi sonni kiritng: "))
#         b = int(input("Ayruvchi sonni kiriting: "))
#         s = a - b
#         print(f"Siz kiritgan {a} dan {b} ni ayrganimizda {s} ga teng bo'ldi ")
# print("Dastur yakunlandi! ")




# print("Tanishlarga taklif noma yuboradigan dastur! ")
# savol = "Foydalanishni istasangiz (ha/yo'q) ni kiriting: "
# while True:
#     qiymat = input(savol)
#     if qiymat.lower() == "yo'q":
#         break
#     elif qiymat.lower() == 'ha':
#         ism = input("Taklifnoma yuborladigan insoning ismini kirting : ")
#         kun = input("Qaysi kunga soat nechiga qayraga borishlarini kiriting : \(Misol uchun: Termiz shaxar yashnobod mahalla 21-a uy soat 8 : 00 ga) :")
#         taklif = f"Assalomu alaykum {ism.title()} aka sizni \n{kun} \nyozlayotgan dasturhonimizga lutfan taklif etamiz !"
#         print(3*("\t"), "Taklifnoma")
#         print(taklif)
#     else:
#         print("Iltimos ha/yo'q deb kiriting matn!")
# print("Dastur yakunlandi! ")


# for i in range(1, 100):
#     if i == 20:
#         break
#     print(f"{i} ning kvadrati {i**2} ga teng")


# print("Assalomu alaykum men 0 dan  m gacha bo'lgan sonlarni kvadratni chiqarishda foydalana olasiz!")
# savol = "Foydalanmoqchi bo'lsangiz (ha/yo'q) bilan tasdiqlang: "
# toplam = []
# for i in range(1, 1000):
#     qiymat = input(savol)
#     if qiymat.lower() == 'ha':
#         son = int(input("Sizga nechigacha sonlar kvadrati kerak: "))
#         for n in range(0, son):
#             toplam.append((n+1) ** 2)
#         print(f"Siz kiritgan {son} gacha sonlarning kvadratni ko'rishingiz mumkun {toplam}")
#     elif qiymat.lower() == "yo'q":
#         break
# print("Dastur tugatildi! ")

















"""
O'zgaruvchilar va ulardagi qoidalar
"""

# O'zgaruvchi nomi harf yoki pastki chiziq (_) bilan boshlanishi kerak
#
# O'zgaruvchi nomi raqam bilan boshlanishi mumkin emas
#
# O'zgaruvchi nomida faqatgina lotin alifbosi harflari (A-z), raqamlar (0-9) va pastki chiziq (_) qatnashishi mumkin
#
# O'zgaruvchi nomida bo'shliq (пробел) bo'lishi mumkin emas
#
# O'zgaruvchi nomida katta-kichik harflar turlicha talqin qilinadi (ism, ISM, va Ism uchta turli o'zgaruvchi)




# ism = "Asomiddin"
# print(ism)

# ism="Shamsiddin"
# print(ism)
# ism = "Azizbek"
# print(ism)

# yosh=19
# ism="Ali"
# ism="Asomiddin"
# print(yosh)
# print(ism)

# for=8
# if=30
# print(if)

# boyi=12
# eni=6
# yuzi=boyi*eni
# print(yuzi)

#
# 1. O'zgaruvchi yaratish
# Yangi o'zgaruvchi name yarating va unga o'zingizning ismingizni bering. So'ngra, uni konsolga chiqarish.
# ism = "Asomiddin"
# print(ism)


# 2. O'zgaruvchini yangilash
# age nomli o'zgaruvchi yarating va unga 30 qiymatini bering. Keyin, age ni 31 ga yangilang va chiqarish.
# age = 30
# age=31
# print(age)


# 3. O'zgaruvchilarni qo'shish
# Ikkita o'zgaruvchi a va b yarating, ularga 15 va 25 qiymatlarini bering. Ularning yig'indisini hisoblang va chiqarish.
# son1=25
# son2=15
# yig=son1+son2
# print(yig)


# 4. Matnni birlashtirish
# first_name va last_name nomli o'zgaruvchilarni yarating. Ularning qiymatlari sifatida o'zingizning ismingiz va familiyangizni bering. Ularni birlashtirib, to'liq ismni chiqarish.
# first_name = "Asomiddin"
# last_name = "Abduqahharov"
# ful_name = last_name +" " + first_name
# print(f"Mening to'liq ismim {ful_name}")



# 5. Foydalanuvchi kiritishi
# Foydalanuvchidan bir son kiritishni so'rang va uni num o'zgaruvchisiga saqlang. Kiritilgan sonni 3 ga ko'paytiring va chiqarish.
# savol =int(input("Assalomu alaykum son kiritinng : " ))
# kop = savol * 3
# print(f"Siz kiritgan {savol} ni 3 ga ko'paytirganimizda {kop} ga teng ")


# 6. O'zgaruvchilarning turini aniqlash
# value nomli o'zgaruvchi yarating va unga "Hello" matnini bering. O'zgaruvchining turini aniqlang va chiqarish.
# matn = "ajidewgiur"
# print(f"Siz kiritgan mat {matn} ning turi {type(matn)}")


# 7. O'zgaruvchilarni taqqoslash
# x va y nomli ikkita o'zgaruvchi yarating va ularga 20 va 30 qiymatlarini bering. Agar x y dan kichik bo'lsa, "x kichik" deb yozing.
# x, y = 20, 30
# print(f" Siz kiritgan {x} va {y} larning kichigi {min(x, y)}")


# 8. O'zgaruvchilarni bo'lish
# a va b o'zgaruvchilarini yarating va ularga 100 va 4 qiymatlarini bering. a ni b ga bo'ling va natijani chiqarish.
# a= 100
# b=4
# print(a/b)



# 9. O'zgaruvchilarni o'zgartirish
# num nomli o'zgaruvchi yarating va unga 50 qiymatini bering. num ni 10 ga kamaytiring va chiqarish.
# num = 50
# num=num-10
# print(num-10)



# 10. Ikkita sonni o'zaro almashish
# x va y nomli ikkita o'zgaruvchi yarating va ularga 8 va 12 qiymatlarini bering. Ularning qiymatlarini o'zaro almashish va natijani chiqarish.
# x=8
# y=12
# x,y=y,x
# print(x, y)


# 11. O'zgaruvchilarni ro'yxatga qo'shish
# numbers nomli bo'sh ro'yxat yarating. Foydalanuvchidan 5 ta son kiritishni so'rang va ularni ro'yxatga qo'shing.
# numbers = []
# for num in range(5):
#     numbers.append(int(input(f"{num+1}-sonni kiriting : ")))
# print(numbers)



# 12. O'zgaruvchilarni ko'paytirish
# a va b o'zgaruvchilarini yarating va ularga 7 va 9 qiymatlarini bering. Ularning ko'paytmasini hisoblang va chiqarish.
# a=7
# b=9
# print(a*b)



# 13. Foydalanuvchi kiritgan matnni tahlil qilish
# Foydalanuvchidan bir matn kiritishni so'rang va uning uzunligini hisoblang va chiqarish.
# mat =input("Assalomu alaykum matn kiriting : ")
# print(f"Siz kiritgan matning uzunlig {len(mat)} ga teng ")




# 14. O'zgaruvchilarni yig'ish
# num1, num2, va num3 nomli uchta o'zgaruvchi yarating va ularga 5, 10, va 15 qiymatlarini bering. Ularning yig'indisini hisoblang va chiqarish.
# num1=5
# num2=10
# num3=15
# print(num1+num3+num2)









# 15. O'zgaruvchini tekshirish
# temperature o'zgaruvchisini yarating. Agar temperature 0 dan past bo'lsa, "Sovuq", 0 dan yuqori bo'lsa "Iliq", 30 dan yuqori bo'lsa "Issiq" deb yozing.
# temp=int(input("Assalomu alaykum tempura turani kiriting : "))
# if temp<0:
#     print(f"{temp} da va bu sovuq degani! ")
# elif temp<30:
#     print(f"{temp} da va bu havo iliq degani! ")
# else:
#     print(f"{temp} da va bu degani havo issiq degani")



# 16. O'zgaruvchilarni o'zaro taqqoslash
# a va b o'zgaruvchilarini yarating va ularga 20 va 20 qiymatlarini bering. Agar ular teng bo'lsa, "Teng" deb yozing.
# a=int(input("Son kiriting: "))
# b=int(input("Ikkinchi sonni kiriting: "))
# if a==b:
#     print(f"Siz kiritgan {a} va {b} sonlar teng ")
#
# else:
#     print(f"Siz kiritgan {a} va {b} solar teng emas")






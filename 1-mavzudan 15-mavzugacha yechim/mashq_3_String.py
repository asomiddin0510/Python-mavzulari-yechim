"""
String (Matn)
"""


# ism="Asomiddin"
# fammilya = "Abduqahharov"
# print(ism)
# print(fammilya)

# ism="Ali"
# familya=" Valiyev"
# ism_familya=ism+familya
# print(ism_familya)

# ism="Jasurbek"
# shahar="Termiz"
# ism_sh=ism, shahar
# print(ism_sh)

# viloyat="Surxondaryo"
# tuman="Termiz"
# v_tuman=viloyat+" "+tuman
# print(v_tuman)

# ism = "Asomiddin"
# yosh = 19
# print("Mening ismim", ism)
# print("Mening yoshim", yosh)
# print("Mening ismim", ism, "yoshim", yosh)


# ism="Abdulloh"
# t_yil="2005"
# print("Uning ismi " + ism)
# print("Uning ismi "+ism+ "tug'ilgan yili " + t_yil)


# f string


# ism="Dilshodbek"
# tuman="Termiz"
# print(f"{ism} hozirda {tuman} yashayapti")

# ism="Sherzod"
# t_yil=1992
# tuman="Termiz"
# print(f"{ism} {t_yil} - yilda {tuman} da tug'ilgan")

# print("Assalomu alaykum men Asomiddin")
# print("Assalomu alaykum \t men Asomiddin")
# print("Assalomu alaykum \n men Asomiddin")



# String metodlar

# ism="asomiddin"
# familya="abduqahharov"
# ism_familya=f"{ism} {familya}"
# print(ism_familya.upper())
# print(ism_familya.lower())
# print(ism_familya.title())
# print(ism_familya.capitalize()



# Bu metodlar matnning boshi va oxiridagi bo'sh joylarni olib tashlaydi.
#
#     lstrip() — matn boshidagi bo'shliqni,
#
#     rstrip() – matn oxiridagi bo'shliqni,
#
#     strip() — matn boshi va oxiridagi bo'shliqlarni olib tashlaydi


# ovqat = "         shashlik           "
# print(ovqat)
# print("Men", ovqat, "ni yoqtraman")
# print("Men", ovqat.lstrip(), "ni yoqtraman")
# print("Men", ovqat.rstrip(), "ni yoqtraman ")
# print("Men", ovqat.strip(), "ni yoqtraman")



#Input haqida va misollar
# ism=input("Ismmingizni kirting hurmatli foydalanuvchi: ")
# print("Assalomu alaykum \n>>> " + ism.title())




    # Stringni aylantirish: Foydalanuvchidan kiritilgan matnni katta harflarga aylantiring.
# matn = input("Assalomu alaykum matn kiriting : ")
# print(matn.upper())

    # Stringni aylantirish: Foydalanuvchidan kiritilgan matnni kichik harflarga aylantiring.
# matn = input("Assalomu alaykum matn kiriting : ")
# print(matn.lower())


    # String uzunligini hisoblash: Foydalanuvchidan kiritilgan matnning uzunligini chiqarish.
# matn = input("Matn kiriting : ")
# print(len(matn))



    # Stringni kesish: Foydalanuvchidan matn va kesish joylarini so'rang, va matnni kesing.
# matn = input("Assalomu alaykum matn kiriting : ")
# savol1 = int(input(f"Kiritgan matningizni qanday bo'lnishini istaysiz bosh indexni kiriting mat uzunligi {len(matn)} ga teng: "))
# savol2=int(input(f"Tugash indexni kiriting : "))
# print(matn[savol1:savol2])


    # Stringni birlashtirish: Ikki alohida matnni foydalanuvchidan olib, ularni birlashtiring.
# matn1=input("Matn kiriting : ")
# matn2=input("Yana matn kiriting : ")
# matn = matn1 + " " + matn2
# print(matn)



    # Stringda qidirish: Foydalanuvchidan matn va qidirilayotgan so'zni so'rang, va so'zning joylashuvini toping.
# text = input("Assalomu alaykum menga matn kiriting: ")
# soz = input("Kerak bo'lgan so'zni kiriting: ")
# # if soz.lower() in text:
#     index=text.index(soz)+len(soz)
#     print(f"Siz kiritgan matn textning [{text.index(soz)}: {index}] indexda joylashgan ")
# else:
#     print(f"Siz kiritgan {soz} textning ichdan topilmadi! ")

# index = text.find(soz)
# if index != -1:
#     index_end = index + len(soz)
#     print(f"Siz kiritgan matn textning [{index}: {index_end}] indexda joylashgan")






    # Stringni almashtirish: Foydalanuvchidan matn, qidirilayotgan so'z va almashtiriladigan so'zni so'rang, so'zni almashtiring.
# text = input("Assalomu alaykum text kiriting: ")
# soz = input("Textning ichdan almashtirmoqchi bo'lgan so'zni kiriting: ").lower()
# almash = input(f"{soz} ni qanday so'zga almashtirmoqchisiz : ").lower()
# if soz in text:
#     text=text.replace(soz, almash)
#     print(text)
# else:
#     print(f"Siz kiritgan {soz} matni textning ichda yo'q ")




    # Stringni bo'sh joydan tozalash: Foydalanuvchidan matnni olib, uning boshidagi va oxiridagi bo'sh joylarni tozalang.
# matn = input("Assalomu alaykum matn kiriting: ")
# print(f"Siz kiritgan matnning ihchamlashgan holatini ko'rishingiz mumkun: {matn.strip()}")



    # Stringni bo'sh joy bilan ajratish: Foydalanuvchidan matnni olib, uni bo'sh joylar bo'yicha ajrating.
# matn = input("Matn kiriting: ")
# for i in matn.split():
#     print(i)





    # Stringni sanash: Foydalanuvchidan kiritilgan matndagi harflar sonini sanang.
# matn = input("Matin kiriting : ")
# n = 0
# for harf in matn:
#     if harf!=" ":
#         n += 1
# print(n)



# matn = " asmiasdi sjafbugfhdsio dsbgjs"
# for i in matn:
#     print(matn)
#     print(i)




    # Stringni teskari aylantirish: Foydalanuvchidan matnni olib, uni teskari aylantiring.







    # Stringni tekshirish: Foydalanuvchidan matnni olib, uning raqam yoki harf ekanligini tekshiring.
    #
    # Stringda harf mavjudligini tekshirish: Foydalanuvchidan matn va harfni olib, harf matnda mavjudligini tekshiring.
    #
    # Stringni kichik harflarga aylantirish va birlashtirish: Foydalanuvchidan ikkita matn olib, ularni kichik harflarga aylantirib birlashtiring.
    #
    # Stringni harflarga ajratish: Foydalanuvchidan matnni olib, harflarga ajrating va ro'yxatga joylashtiring.
    #
    # Stringni o'zgartirish: Foydalanuvchidan matnni olib, har bir 'a' harfini 'o' ga o'zgartiring.
    #
    # Stringda so'zlarni sanash: Foydalanuvchidan matnni olib, undagi so'zlar sonini sanang.
    #
    # Stringni formatlash: Foydalanuvchidan ism va yoshni olib, "Mening ismim {ism} va men {yosh} yoshdaman." formatida chiqarish.
    #
    # Stringni tekshirish: Foydalanuvchidan matnni olib, uning barcha harflari katta ekanligini tekshiring.
    #
    # Stringni alifbo tartibida chiqarish: Foydalanuvchidan matnni olib, harflarni alifbo tartibida chiqarish.
    #
    # Stringda raqamlarni sanash: Foydalanuvchidan matnni olib, undagi raqamlar sonini sanang.
    #
    # Stringni qidirish va almashtirish: Foydalanuvchidan matn, qidirilayotgan so'z va almashtiriladigan so'zni so'rang, va natijani chiqarish.
    #
    # Stringni bo'sh joy bilan ajratish va ro'yxatga joylashtirish: Foydalanuvchidan matnni olib, uni bo'sh joylar bo'yicha ajratib ro'yxatga joylashtiring.
    #
    # Stringni harf bo'yicha ajratish: Foydalanuvchidan matnni olib, harflarni alohida chiqarish.
    #
    # Stringni bir xil harflar bilan almashtirish: Foydalanuvchidan matnni olib, 'e' harfini '3' ga almashtiring.
    #








































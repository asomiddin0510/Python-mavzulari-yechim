"""
Listlar(Ro'yxatlar) bilan ishlash

"""


# mevalar=['anaor', 'olcha', 'olma', 'gilos', 'shaftoli', 'kivi', "o'rik", "zardoli"]
# print(mevalar)
# print(mevalar[:4])
# print(mevalar[1:5])
#
# narxlar=[12000, 14000, 14500, 18000, 23000, 34000, 29000, 36000]
# print(len(mevalar))
# print(len(narxlar))
#
# print(f"Siz haritqilgan {mevalar[2:4]} ning narxlari {narxlar[2:4]}  dan")


# mashinalar=["Bugati", 'mersedes', 'BNW', "nexia", 'damas', 'volga']
# print(mashinalar[1].upper())
# print(mashinalar[3].upper())
# print(mashinalar[4].title())
# print(mashinalar[2].lower())
# print(mashinalar[2].capitalize())


# narxlar=[12, 34, 56, 23, 56, 46, 78, 67, 78, 49, 59]
# som=narxlar[3]+narxlar[5]
# print(som)

# poliz=['tarvuz', 'qovun', 'qovoq', 'bodring', 'pamidor']
# poliz[0]="ko'kat"
# print(poliz)

# poliz=['tarvuz', 'qovun', 'qovoq', 'bodring', 'pamidor']
# poliz[2]="lovlagi"
# print(poliz)


# poliz=['tarvuz', 'qovun', 'qovoq', 'bodring', 'pamidor']
# poliz.append("olma")
# poliz.append(["olma", "olcha", 'banan'])
# print(poliz)

# poliz=['tarvuz', 'qovun', 'qovoq', 'bodring', 'pamidor']
# mevalar=['meva10', 'meva2', 'meva3', 'meva4']
# poliz.append(mevalar)
# print(poliz)


# poliz=['tarvuz', 'qovun', 'qovoq', 'bodring', 'pamidor']
# mevalar=['meva10', 'meva2', 'meva3', 'meva4']
# print(mevalar,poliz)
# print(mevalar+poliz)



# mevalar=['meva10', 'meva2', 'meva3', 'meva4']
# mevalar.insert(0, 'daraxt')
# print(mevalar)




# poliz=['tarvuz', 'qovun', 'qovoq', 'bodring', 'pamidor']
# poliz.insert(3, "olx'ri")
# print(poliz)


# cars=[]
# cars.append("BNW")
# cars.insert(0, 'nexia')
# print(cars)


# colors=[]
# colors.append("sariq")
# colors.append("qizil")
# colors.append("yashil")
# colors.append("qora")
# colors.insert(2, "ko'k")
# colors[2]='binafsha'
#
# print(colors)


# collors=['sariq', 'yashil', 'qora', "ko'k", 'binafsha']
# del collors[0]
# del collors[1]
# print(collors)





# collors=['sariq', 'yashil', 'qora', "ko'k", 'binafsha']
# del collors[2]
# collors.append("sariq")
# print(collors)


# collors=['sariq', 'yashil', 'qora', "ko'k", 'binafsha']
# collors.remove('sariq')
# collors.remove("ko'k")
# print(collors)




# collors=['sariq', 'yashil', 'qora', "ko'k", 'binafsha']
# pop=collors.pop(0)
# print(collors)
# print(pop)




# collors=['sariq', 'yashil', 'qora', "ko'k", 'binafsha', "anor", 'bexi', 'savdo']
# collors.sort()
# print(collors)



# collors=['sariq', 'yashil', 'qora', "ko'k", 'binafsha', "anor", 'daraxt']
# collors.sort(reverse=True)
# print(collors)



# collors=['sariq', 'yashil', 'qora', "ko'k", 'binafsha', "anor", 'daraxt']
# collors1=sorted(collors)
# print(collors1)
# print(collors)


# collors=['sariq', 'yashil', 'qora', "ko'k", 'binafsha', "anor", 'daraxt']
# collors1=sorted(collors, reverse=True)
# print(collors1)
# print(collors)




"""### List (Ro'yhat) haqida tushuncha

**List** (ro'yhat) Python dasturlash tilida keng qo'llaniladigan ma'lumot tuzilmasi bo'lib, u tartiblangan va o'zgartiriladigan elementlar to'plamini ifodalaydi. Ro'yhatlar kvadrat qavslar `[]` ichida yaratiladi va elementlar vergul `,` bilan ajratiladi. Ro'yhatlar turli xil ma'lumot turlarini o'z ichiga olishi mumkin, masalan, butun sonlar, satrlar, boshqa ro'yhatlar va hokazo.

#### Ro'yhat yaratish
```python
my_list = [1, 2, 3, 'apple', 'banana']
```

#### Ro'yhat elementlariga murojaat qilish
```python
print(my_list[0])  # 1
print(my_list[3])  # 'apple'
```

#### Ro'yhat elementlarini o'zgartirish
```python
my_list[1] = 'orange'
print(my_list)  # [1, 'orange', 3, 'apple', 'banana']
```

#### Ro'yhatga element qo'shish
```python
my_list.append('cherry')
print(my_list)  # [1, 'orange', 3, 'apple', 'banana', 'cherry']
```

#### Ro'yhatdan element olib tashlash
```python
my_list.remove('apple')
print(my_list)  # [1, 'orange', 3, 'banana', 'cherry']
```

#### Ro'yhat uzunligini aniqlash
```python
print(len(my_list))  # 5
```

### Ro'yhatlar bilan bog'liq 20 ta masala

1. **Ro'yhat yaratish**: Bo'sh ro'yhat yarating va unga 5 ta element qo'shing.
2. **Ro'yhat elementlarini chiqarish**: Ro'yhatdagi barcha elementlarni birma-bir chiqarib bering.
3. **Ro'yhat uzunligini aniqlash**: Ro'yhat uzunligini aniqlang va chop eting.
4. **Ro'yhat elementini o'zgartirish**: Ro'yhatdagi ikkinchi elementni o'zgartiring.
5. **Ro'yhatga element qo'shish**: Ro'yhat oxiriga yangi element qo'shing.
6. **Ro'yhatdan element olib tashlash**: Ro'yhatdan birinchi uchraydigan elementni olib tashlang.
7. **Ro'yhatni tartiblash**: Ro'yhatdagi sonlarni o'sish tartibida tartiblang.
8. **Ro'yhatni teskari tartiblash**: Ro'yhatni teskari tartibda chiqaring.
9. **Ro'yhatni tozalash**: Ro'yhatni tozalang (barcha elementlarni olib tashlang).
10. **Ro'yhatni nusxalash**: Ro'yhatni yangi ro'yhatga nusxalash.
11. **Ro'yhatni birlashtirish**: Ikki ro'yhatni birlashtirib yangi ro'yhat yarating.
12. **Ro'yhat elementlarini sanash**: Ro'yhatda ma'lum bir element necha marta uchrashini aniqlang.
13. **Ro'yhatni kesish**: Ro'yhatning bir qismini kesib oling (slicing).
14. **Ro'yhatda element borligini tekshirish**: Ro'yhatda ma'lum bir element borligini tekshiring.
15. **Ro'yhat indeksini aniqlash**: Ro'yhatda ma'lum bir elementning indeksini aniqlang.
16. **Ro'yhatni qayta tartiblash**: Ro'yhatni o'sish tartibida qayta tartiblang va chop eting.
17. **Ro'yhat elementlarini aylantirish**: Ro'yhat elementlarini aylantirib yangi ro'yhat yarating.
18. **Ro'yhatga element qo'shish (insert)**: Ro'yhatning ma'lum bir joyiga yangi element qo'shing.
19. **Ro'yhatni ko'paytirish**: Ro'yhatni bir necha marta takrorlab yangi ro'yhat yarating.
20. **Ro'yhatni stringga aylantirish**: Ro'yhatni stringga aylantirib chop eting.

Ushbu masalalarni yechish orqali siz ro'yhatlar bilan ishlashni yaxshi o'rganishingiz mumkin. Har bir masalani mustaqil ravishda yechib ko'ring va Python kodini yozing. Agar biror bir masalada qiyinchilikka duch kelsangiz, yordam so'rashdan tortinmang!"""








"""Quyidagi mashqlarni bajaring:

    ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting

    Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring: 

    sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik). 

    Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring. 

    t_shaxslarva z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting. 

    Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (
    .pop()
    ), quyidagi ko'rinishda chiqaring:

    friendsnomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting. 

    Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang. 

    Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.

    Yangi mehmonlardeb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing."""








































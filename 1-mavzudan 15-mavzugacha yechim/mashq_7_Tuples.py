"""
TUPLES haqida
TUPLES - O'ZGARMAS RO'YXAT

Dastur yaratish davomida o'zgarmas ro'yxat tuzish talab qilinishi mumkin.
Pythonda bunday ro'yxatlar tuples deb yuritiladi. Tuple ichidagi qiymatlarni bir marta,
dastur boshida beriladi va so'ngra o'zgartirib bo'lmaydi. List dan farqli ravishda,
Tuple e'lon qilishda kvadrat qavslar [] o'rniga oddiy qavslar () ishlatiladi:

"""

# mashinalar=('kobolt', 'lasetti', 'nexia', 'damas', 'jentra', 'malibu')
# print(type(mashinalar))



# mashinalar=('kobolt', 'lasetti', 'nexia', 'damas', 'jentra', 'malibu')
# mashinalar.remove("kobolt")
# print(mashinalar)


# mashinalar=('kobolt', 'lasetti', 'nexia', 'damas', 'jentra', 'malibu')
# mashinalar_list=list(mashinalar)
# mashinalar_list.append("kaptiva")
# print(type(mashinalar_list))
# mashinalar=tuple(mashinalar_list)
# print(mashinalar)
# print(type(mashinalar))


"""### Tuple (Turkum) haqida tushuncha

**Tuple** (turkum) Python dasturlash tilida tartiblangan va o'zgarmas (immutable) elementlar to'plamini ifodalaydi. Tuple'lar oddiygina qavslar `()` ichida yaratiladi va elementlar vergul `,` bilan ajratiladi. Tuple'lar ro'yhatlarga o'xshash, lekin ularning asosiy farqi shundaki, tuple'lar o'zgarmas, ya'ni yaratilgandan keyin ularning elementlarini o'zgartirib bo'lmaydi.

#### Tuple yaratish
```python
my_tuple = (1, 2, 3, 'apple', 'banana')
```

#### Tuple elementlariga murojaat qilish
```python
print(my_tuple[0])  # 1
print(my_tuple[3])  # 'apple'
```

#### Tuple uzunligini aniqlash
```python
print(len(my_tuple))  # 5
```

#### Tuple ichida bir elementli tuple yaratish
```python
single_element_tuple = (5,)  # Vergul qo'yish majburiy
print(single_element_tuple)  # (5,)
```

#### Tuple ichida tuple yaratish (nested tuples)
```python
nested_tuple = (1, 2, (3, 4), 5)
print(nested_tuple[2])  # (3, 4)
print(nested_tuple[2][1])  # 4
```

### Tuple'lar bilan bog'liq 20 ta masala

1. **Tuple yaratish**: Bo'sh tuple yarating va unga 5 ta element qo'shing.
2. **Tuple elementlarini chiqarish**: Tuple'dagi barcha elementlarni birma-bir chiqarib bering.
3. **Tuple uzunligini aniqlash**: Tuple uzunligini aniqlang va chop eting.
4. **Tuple ichida bir elementli tuple yaratish**: Bir elementli tuple yarating.
5. **Tuple ichida tuple yaratish**: Tuple ichida yana bir tuple yarating va unga murojaat qiling.
6. **Tuple elementlarini sanash**: Tuple'da ma'lum bir element necha marta uchrashini aniqlang.
7. **Tuple indeksini aniqlash**: Tuple'da ma'lum bir elementning indeksini aniqlang.
8. **Tuple'ni ko'paytirish**: Tuple'ni bir necha marta takrorlab yangi tuple yarating.
9. **Tuple'ni birlashtirish**: Ikki tuple'ni birlashtirib yangi tuple yarating.
10. **Tuple'ni kesish**: Tuple'ning bir qismini kesib oling (slicing).
11. **Tuple ichida ro'yhat yaratish**: Tuple ichida ro'yhat yaratib, unga murojaat qiling.
12. **Tuple ichida tuple yaratish va element qo'shish**: Tuple ichida tuple yaratib, yangi element qo'shing.
13. **Tuple ichida tuple yaratish va element olib tashlash**: Tuple ichida tuple yaratib, element olib tashlang.
14. **Tuple ichida element borligini tekshirish**: Tuple'da ma'lum bir element borligini tekshiring.
15. **Tuple'ni stringga aylantirish**: Tuple'ni stringga aylantirib chop eting.
16. **Tuple ichida string yaratish**: Tuple ichida string yaratib, unga murojaat qiling.
17. **Tuple ichida ro'yhat va tuple yaratish**: Tuple ichida ro'yhat va tuple yaratib, ularni birma-bir chiqarib bering.
18. **Tuple ichida elementlarni tartiblash**: Tuple ichidagi elementlarni tartiblang.
19. **Tuple ichida dictionary yaratish**: Tuple ichida dictionary yaratib, unga murojaat qiling.
20. **Tuple'ni o'zgartirish (indirectly)**: Tuple'ni ro'yhatga aylantirib, o'zgartirib, yana tuple'ga aylantiring.

Ushbu masalalarni yechish orqali siz tuple'lar bilan ishlashni yaxshi o'rganishingiz mumkin. Har bir masalani mustaqil ravishda yechib ko'ring va Python kodini yozing. Agar biror bir masalada qiyinchilikka duch kelsangiz, yordam so'rashdan tortinmang!"""













"""### Set (To'plam) haqida tushuncha

**Set** (to'plam) Python dasturlash tilida tartiblanmagan va takrorlanmas elementlar to'plamini ifodalaydi. Set'lar qavslar `{}` ichida yaratiladi va elementlar vergul `,` bilan ajratiladi. Set'lar ichida bir xil qiymatli elementlar takrorlanmaydi va ularning tartibi yo'q.

#### Set yaratish
```python
my_set = {1, 2, 3, 'apple', 'banana'}
```

#### Set yaratish (bo'sh set)
```python
empty_set = set()
```

#### Setga element qo'shish
```python
my_set.add('cherry')
```

#### Setdan element olib tashlash
```python
my_set.remove('banana')
```

#### Setning uzunligini aniqlash
```python
print(len(my_set))  # 5
```

#### Set ichida element borligini tekshirish
```python
print('apple' in my_set)  # True
```

#### Setlar orasidagi kesishma (intersection)
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 & set2)  # {3}
```

#### Setlar orasidagi birlashma (union)
```python
print(set1 | set2)  # {1, 2, 3, 4, 5}
```

### Set'lar bilan bog'liq 20 ta masala

1. **Set yaratish**: Bo'sh set yarating va unga 5 ta element qo'shing.
2. **Set elementlarini chiqarish**: Set'dagi barcha elementlarni birma-bir chiqarib bering.
3. **Set uzunligini aniqlash**: Set uzunligini aniqlang va chop eting.
4. **Setga element qo'shish**: Setga yangi element qo'shing.
5. **Setdan element olib tashlash**: Setdan element olib tashlang.
6. **Set ichida element borligini tekshirish**: Setda ma'lum bir element borligini tekshiring.
7. **Setlarni birlashtirish**: Ikki setni birlashtirib yangi set yarating.
8. **Setlar orasidagi kesishmani aniqlash**: Ikki set orasidagi kesishmani aniqlang.
9. **Setlar orasidagi farqni aniqlash**: Ikki set orasidagi farqni aniqlang.
10. **Setni tozalash**: Setni tozalang (bo'shatish).
11. **Setdan tasodifiy element olib tashlash**: Setdan tasodifiy element olib tashlang.
12. **Setni ro'yhatga aylantirish**: Setni ro'yhatga aylantirib chop eting.
13. **Ro'yhatni setga aylantirish**: Ro'yhatni setga aylantirib chop eting.
14. **Set ichida set yaratish**: Set ichida yana bir set yaratib, unga murojaat qiling.
15. **Setda takroriy elementlarni aniqlash**: Ro'yhatdagi takroriy elementlarni setga aylantirib aniqlang.
16. **Setlar orasidagi simmetrik farqni aniqlash**: Ikki set orasidagi simmetrik farqni aniqlang.
17. **Setga bir nechta element qo'shish**: Setga bir nechta elementni qo'shing (update metodidan foydalaning).
18. **Set ichida string yaratish**: Set ichida string yaratib, unga murojaat qiling.
19. **Set ichida ro'yhat va tuple yaratish**: Set ichida ro'yhat va tuple yaratib, ularni birma-bir chiqarib bering.
20. **Setni stringga aylantirish**: Setni stringga aylantirib chop eting.

Ushbu masalalarni yechish orqali siz set'lar bilan ishlashni yaxshi o'rganishingiz mumkin. Har bir masalani mustaqil ravishda yechib ko'ring va Python kodini yozing. Agar biror bir masalada qiyinchilikka duch kelsangiz, yordam so'rashdan tortinmang!"""


























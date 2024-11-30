"""
Son top o'yini
"""

import random as rand

from numpy.f2py.symbolic import eliminate_quotes


# def son_top1() :
#     print("Keling biz siz bilan son topish o'yini o'ynaymiz! \nMen son o'ylayman siz topishga urnib ko'rasiz ")
#     ihtiyoriy_son1 = rand.randint(1, 15)
#     savol1 = int(input("1 dan 15 gacha son o'yladim. Topa olsizmi : "))
#     n1 = 0
#     while True :
#         n1 += 1
#         if savol1 < ihtiyoriy_son1 :
#             print(f"Xato men o'ylagan son {savol1} dan katta! ", end="")
#
#         elif savol1 > ihtiyoriy_son1 :
#             print(f"Xato men o'ylagan son {savol1} dan kichik ! ", end="")
#
#         elif savol1 == ihtiyoriy_son1 :
#             return f"Tabriklayman {n1} ta urnishda topdingiz! Men o'ylagan son {ihtiyoriy_son1} edi.", n1
#
#         savol1 = int(input("Yana harakat qilib ko'ring : "))
#
#
#
#
#
#
# def son_top2() :
#     boshlash = input("Keling endi siz son o'ylaysiz men topishga urnib ko'raman. \n1 dan 15 gacha o'ylang agar o'ylagan bo'lsangiz 'Enter' tugmasni bosing! ")
#     istalgan_son2 = rand.randint(1,15)
#     n2 = 0
#
#     if boshlash == '' :
#
#         while True :
#             n2 += 1
#             savol2 = input(f"Siz o'ylagan son {istalgan_son2}. \nTo'g'ri bo'lsa: 'yes'. \nKatta bo'lsa: 'big'. \nKichik bo'lsa: 'small' kiriting : ")
#
#             if savol2.lower() == 'big' :
#                 istalgan_son2 = rand.randint(istalgan_son2+1, 15)
#
#             elif savol2.lower() == 'small' :
#                 istalgan_son2 = rand.randint(1, istalgan_son2-1)
#
#             elif savol2.lower() == 'yes' :
#                 return f"Siz o'ylagan son {istalgan_son2} edi. Men {n2} ta urnishda toppdim!" , n2
#
#
#
#
#
#
#
# def play() :
#         savol = input("O'yinni boshlashni istasangiz 'start' deb yozing: ")
#         while True :
#             if savol.lower() == 'start' or savol == 'ha' :
#                 start1, n1 = son_top1()
#                 start2, n2 = son_top2()
#                 print(start1, n1)
#                 print(start2, n2)
#                 if n1 == n2 :
#                     print(f"O'yin {n1} taga : {n2} ta urnish bilan durrang bo'lib yakunlandi!")
#                 elif n1 < n2 :
#                     print(f"O'yinda {n1} taga : {n2} ta urnish bilan siz g'alaba qozondingiz!")
#                 elif n1 > n2 :
#                     return f"O'yin {n1} taga : {n2} ta urnish bilan men g'alaba qozondim!"
#                 savol = input("Yana o'ynaymizmi (ha/yo'q) kiritng ")
#                 if savol.lower() == "yo'q" :
#                     break
# print(play())














def son_top(x = 15) :

    input("Keling o'yin o'ynaymiz. Men son o'ylayman siz topasiz boshlash uchun 'Enter'ni bosing. ")
    taxminiy_son = rand.randint(1, x)

    print(f"1 dan {x} gacha son o'yladim topishga urnib ko'ring ? ", end="")
    taxminlar = 0

    while True :
        taxminlar += 1
        foy_soni = int(input(" Sonni kiriting : "))

        if foy_soni < 1 or foy_soni > x :
            print(f"Men {1, x} oraliqda son o'ylaganman qayta ", end="")
            continue

        if foy_soni < taxminiy_son :
            print(f"Men o'ylagan son {foy_soni} dan katta. Yana urnib ko'ring ", end="")

        elif foy_soni > taxminiy_son :
            print(f"Men o'ylagan son {foy_soni} dan kichik . Yana urinib ko'ring ", end="")

        else :
            break
    print(f"Men o'ylagan son {taxminiy_son} ga teng tabriklayman siz uni {taxminlar} ta urnishda topdingiz! ")
    return taxminlar





def son_top_mash(y = 15) :

    input(f"1 dan {y} gacha son o'ylang. O'ylagan bo'lsangiz 'Enter' tugmasni bosing. ")
    taxminlar = 0

    quyi = 1
    yuqori = y

    while True :

        taxminiy_son = rand.randint(quyi, yuqori)
        taxminlar += 1

        savol = input(f"Siz o'ylagan son {taxminiy_son} ga teng. to'g'ri (T) men o'ylagan son bundan kattaroq (+) , men o'ylagan son kichikroq (-) ? ")

        if savol == '+' :
            quyi = taxminiy_son + 1

        elif savol == '-' :
            yuqori = taxminiy_son-1

        else:
            break

    print(f"Sonigizni {taxminlar} ta taxmin bilan topdim!")
    return taxminlar





def play() :
    while True:

        n1 = son_top()
        n2 = son_top_mash()

        if n1 > n2 :
            print(f"Meni tabriklang men yutdim! hisob {n1} : {n2} ")
        elif n2 > n1 :
            print(f"Tabriklayman siz yutdingiz! hisob {n2} : {n1} ")
        else :
            print(f"Durrang! hisob {n2} : {n1}")
        savol = input("Yana o'ynaymizmi : ")
        if savol.lower() != "ha" :
            break
        print("O'yin tugadi!")

play()

































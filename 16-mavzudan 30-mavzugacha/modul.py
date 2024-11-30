"""
19-mavzudagi darsada kerak bo'ladigan funksiyalar kodi
"""



def avto_royxat(modeli, rangi, kompanyasi, yurgani, yili, narxi = None ) :
    royxat = {
        'Modeli' : modeli,
        'Rangi': rangi,
        'Kompanyasi' : kompanyasi,
        'Yurgan yo\'li' : yurgani ,
        'Chiqarilgan' : yili,
        'Narxi'  : narxi
    }
    return royxat




def royxatni_tuz() :
    print("Quyidagi malumotlarni kiritish orqali siz avtomobillar ro'yxatni shakillantrishingiz mumkun !")
    cars = []
    while True :
        model = input("Avtomobilning modelini kiriting : ")
        rang = input("Rangni kiriting : ")
        kompanya = input("Kompanyasini kiriting : ")
        masofa = int(input("Yurgan yo'lini kiriting : "))
        yil = int(input("Chiqarilgan yilini kiriting : "))
        narx = int(input("Narxni kiriting : "))
        cars.append(avto_royxat(model, rang, kompanya, masofa, yil, narx))
        savol = input("Dasturni to'xtatmoqchi bo'lsangiz (exit) \nDavom etmoqchi bo'lsangiz (go) ni kiriting ")
        if savol.lower() == 'exit' :
            break
    return cars




def royxat_chiqar(cars) :
    print("Salondagi avtomobillar ro'yxatni quyda ko'rishingiz mumkun !")
    n = 0
    for avto in cars :
        n += 1
        print(f"{n}-avtomobil haqida malumotlar: \n"
                f"Modeli : {avto['Modeli'] } , Ishlab chiqargan kompaniya nomi : {avto['Kompanyasi']} , "
                f"Rangi : {avto['Rangi']}, Yurgan yo'li : {avto['Yurgan yo\'li']} km , "
                f"Ishlab chiqarilgan yili : {avto['Chiqarilgan']}-yil, Narxi : {avto['Narxi']} ming ")


if __name__ == "__main__":
    cars = royxatni_tuz()
    royxat_chiqar(cars)
























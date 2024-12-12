from uuid import uuid4

class Avto :
    def __init__(self, make, model, rang, yil, narx, km = 0) :
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narx = narx
        self.__km = km
        self.__id = uuid4()

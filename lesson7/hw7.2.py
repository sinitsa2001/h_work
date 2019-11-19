

class Clothes:
    def __init__(self, param):
        self.param = param

    @property
    def clothes_metod(self):
        return f'Параметр расчета одежды {self.param}'


cl = Clothes('by Trusselia')
print(cl.param)
print(cl.clothes_metod)


class Coat(Clothes):
    def init(self, param):
        Clothes.__init__(self, param)

    def coat_metod(self):
        return f'Для пошива Вашего пальто {cl.param}потребуется: {round((self.param / 6.5 + 0.5), 2)} погонных метра ткани'


cl_1 = Coat(int(input('Введите размер пальто: ')))
print(cl_1.coat_metod())


class Suit(Clothes):
    def init (self, param):
        Clothes.__init__(self, param)

    def suit_metod(self):
            return f'Для пошива Вашего костюма {cl_2.param}потребуется: {round((self.param * 2  + 0.3), 2)} погонных метра ткани'

cl_2 =Suit(int(input('Введите параметр костюма')))
print(cl_2.suit_metod())

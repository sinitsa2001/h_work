#Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.


class Stationery:
    def __init__(self, title):
        self.title = title
    def draw_metod(self):
        print('%s Запуск отрисовки.'% self.title )

class Pen(Stationery):

    def draw_metod(self):
        print('%s Pen..ский метод отрисовки'% self.title )

class Pencil(Stationery):

    def draw_metod(self):
        print('%s Pencil..ский метод дорисовки'% self.title )

class Handle(Stationery):

    def draw_metod(self):
        print('%s Handle..ский метод прорисовки'% self.title )

test = Stationery('Базовый')
test.draw_metod()

p = Pen('Ручка')
p.draw_metod()

p1 = Pencil('Карандаш')
p1.draw_metod()

p2 = Handle('Маркер')
p2.draw_metod()


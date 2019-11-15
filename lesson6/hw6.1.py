# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
# и метод running (запуск). Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только
# в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав
# экземпляр и вызвав описанный метод.
# Родительский метод класса Transport
# Родительский метод класса Auto
# Родительский метод класса Bus

# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении
# выводить соответствующее сообщение и завершать скрипт.

import time
class TrafficLight:
    color = 'цвет'
    def running(self, red, green, yellow):
        print('Светофор показывает цвет: ')
        self.red = red
        self.green = green
        self.yellow = yellow
a = TrafficLight()
a.running('red', 'green', 'yellow')
timer = 16
while True:
    time.sleep(0.985)
    start = time.time()
    if timer <=16 and timer >9:
        print(a.red)
        print(timer)
        timer -= 1
    if timer <=9 and timer >7:
        print(a.yellow)
        print(timer)
        timer -= 1
    if timer <=7 and timer >0:
        print(a.green)
        print(timer)
        timer -= 1
    if timer == 0:
        timer = 16


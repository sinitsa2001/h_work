'''
Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и
умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса
(комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.

'''
import math
class Complex_digit:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        #self.a = complex(1,2)
        #self.b = complex(3,4)
    def __add__(self, other):
        return self.a + other.a, self.b + other.b
    def __str__(self):
        return self.a, self.b

mc_1 = complex(1,2)
mc_2 = complex(3,4)
mc_3 = mc_1+mc_2
mc_4 = mc_1 - mc_2
mc_5 = mc_1 * mc_2
print(mc_3)
print(mc_4)
print(mc_5)

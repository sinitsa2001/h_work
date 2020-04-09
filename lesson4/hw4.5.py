#Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
#Подсказка: использовать функцию reduce().
from functools import reduce

new_list = [el for el in range(100,1002) if el % 2 == 0]
print(new_list)
multiplier_all = reduce(lambda x, y: x * y, new_list)

print(multiplier_all)
# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


arg_1 = int(input('Введите целое число: '))
arg_2 = int(input('Введите целое число: '))
arg_3 = int(input('Введите целое число: '))

def summ_max_two_args(a1,a2,a3):
    my_list = [a1,a2,a3]
    min_el = min(my_list)

    summ_max = a1 + a2 + a3 - min_el
    return summ_max

print(summ_max_two_args(arg_1,arg_2,arg_3))

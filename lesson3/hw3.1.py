

arg_1 = int(input('Введите делимое число: '))
arg_2 = int(input('Введите делитель: '))

def my_func(arg_1, arg_2):

    try:
        my_div = 0
        my_div = arg_1 / arg_2
    except ZeroDivisionError:
        print('Не делим на ноль!!')
    return my_div

print (round(my_func(arg_1,arg_2),2))
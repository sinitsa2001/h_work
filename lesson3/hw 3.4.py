'''Программа принимает действительное положительное число x и целое отрицательное число y.
 Необходимо выполнить возведение числа x в степень y.
 Задание необходимо реализовать в виде функции my_func(x, y).
 При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **,
предусматривающая использование цикла.'''


#!!! не справился с вариантом 2...не могу решить через цикл..
#логику вроде понимаю...а сделать не могу

x = int(input('Введите целое положительное число: '))
y = int(input('Введите целое отрицательное число: '))
def my_exponent():
    res = (x**y)
    return res
print(round(my_exponent(),3))

x = int(input('Введите целое положительное число: '))
y = int(input('Введите целое отрицательное число: '))
numbers = [x]
print(list(map(lambda x: x**y,numbers)))



'''x = int(input('Введите целое положительное число: '))
y = int(input('Введите целое отрицательное число: '))

param = (x,y)
print(param)

def m_2():
    
    for i in (param):
        res = x*x
        i-=1
        return res

print(x)

    #return x
#print(my_exponent()'''



'''num_1 = int(input('Введите целое положительное число: '))
num_2 = int(input('Введите целое отрицательное число: '))
numbers = [num_1,num_2]
print(numbers)
def m_2 (numbers):
    global num_1,num_2
    for num_1,num_2 in (numbers):
        num_1 = num_1*num_1
        num_2 = num_2 -1
    return num_1
    #print(y)
    print(m_2(num_1))'''

#x*=x
#print(x)'''
'''def my_exponent():
    global y
    print(y)
    i == y
        while (i > 0):
            res = x*x
        #y = y - 1
        i = y-1
            return res
print(my_exponent())'''

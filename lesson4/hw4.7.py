#Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fibo_gen().
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые 15 чисел.
#Подсказка: факториал числа n — произведение чисел от 1 до n.
# Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
from math import factorial

print(factorial(4))

def factorial(n):
    if n == 1:
        yield 1
    else:
        yield n * factorial(n-1)

print(factorial(6))


#  еще один вариант
fibo_gen = (1)

def fibo_gen():
    for el in fibo_gen():
        yield el * factorial(el-1)
g = fibo_gen()
print(g)
for el in g:
    print(el)





'''def factorial_verbose(number):
    for i in range(number):
            yield f'{i + 1} x '

res = ''.join([x for x in factorial_verbose(5)])
res = ' '.join([res[:len(res)-3], '=', str(math.factorial(5))])
#res '1 x 2 x 3 x 4 x 5 = 120'
'''



#generator = (param * param for param in range(5))
#for el in generator:
#    print(el)

#print(next(generator))

'''def generator():
    for el in (10, 20, 30):
        yield el
g = generator()
print(g)
for el in g:
    print(el)'''
#Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fibo_gen().
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые 15 чисел.
#Подсказка: факториал числа n — произведение чисел от 1 до n.
# Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

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


def fido_gen():
    for el in fido_gen(1):
        yield el
g = generator()
print(g)
for el in g:
    print(el)
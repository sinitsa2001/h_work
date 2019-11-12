#Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
#Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Для формирования списка использовать генератор.
from functools import reduce
from collections import Counter

assert isinstance(randint,object )
from random import randint

mylist = [randint(-10, 10) for i in range(20)]
#mylist = [2,32,33,50,50,3,3, 5,7,20, 30, 25, 20]
for i in range(len(mylist)-1):
    n = int(mylist[i])
    i+=1
    m = int(mylist[i])
    if m > n:
        n = m
        print(m, end=' ')

# решение второе
for i in range(len(mylist)):
    if mylist[i]>mylist[i-1] and i!=0:
        print(mylist[i])






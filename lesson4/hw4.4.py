#Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.

from collections import Counter
mylist = [2,32,33,50,50,3,3, 5,7,20, 30, 25, 20]
my_new_list =[k for k,v in Counter(mylist).items() if v<=1]
print(my_new_list)
# подсмотрел в инете...решение работает и понятно как. также можно вывести дубликаты = поменяв знак в последнем if


my_list = [10, 10, 3, 4, 5, 9, 30, 30]
#z = ['a', 'b', 'a', 'c', 'b', 'a', ]
new_list = [my_list[i] for i in range(len(my_list)) if i == my_list.index(my_list[i])]
# выводит элементы списка НЕ сортирую, но без дублирующих (удаляет дубликаты)!! найти другое решение
print(new_list)

print(list(set(my_list)))
# тоже удаляет дубликаты = но при этом делает сортировку !! не подходит


# !! ВОТ НЕ ПЛОХОЕ РЕШЕНИЕ - ТОЛЬКО НЕ ПОЙМУ = КАК ПЕРЕВЕСТИ ИНДЕКСЫ В ЗНАЧЕНИЯ БЕЗ СОЗДАНИЯ СЛОВАРЯ
#ЕСЛИ ЕСТЬ КАКОЕ ТО РЕШЕНИЕ В ДАННОМ СЛУЧАЕ = БУДУ ПРИЗНАТЕЛЕН ЗА ПОДСКАЗКУ
new_list = [el for el in (my_list) if el in my_list]
list_1 =[i for i, x in enumerate(my_list) if my_list.count(x) > 1]
# выводит индексы повторяющихся элементов
list_2 = [i for i,x in enumerate(my_list) if my_list.count(x)<=1]
# выводит индексы не повторающихся элементов
print(list_1)
print(list_2)
#print(list_2.index([my_list]))
#print(list_1.index[1:4])
#print(new_list)


'''mylist = [2,32,33,50,50,3,3, 5,7,20, 30, 25, 20]
list_3 = [i for i,x in mylist if my_list.count(x)<=1]
print(list_3)'''


from random import randint

my_list = [randint(5, 10) for i in range(4)]
list_2 = [i for i, x in enumerate(my_list) if my_list.count(x) <= 1]
print(my_list)
print(list_2)
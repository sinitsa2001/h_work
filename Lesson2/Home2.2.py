#Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

# не понимаю - как завести в цикл...не работает,
# ну и с нечетным тоже не все понятно
# ...вроде как должно...проверяю = не понятно))
my_list = [1,2,3,4,5,6,7,8,9]
print(my_list[-1])
for i in range(len(my_list)):
    my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
    #my_list[2], my_list[3] = my_list[3], my_list[2]
    #my_list[4], my_list[5] = my_list[5], my_list[4]
    #my_list[6], my_list[7] = my_list[7], my_list[6]
    if my_list[-1] // 2 != 0:
        break
    elif my_list[-1] //2 ==0:
        continue
print(my_list)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(1, len(my_list)):
    my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]
    i+=2

    print(my_list)
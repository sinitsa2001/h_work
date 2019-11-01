#Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.
my_list = input('Введите несколько слов. Разделите слова пробелами: ')
my_list = my_list.split()
l = len(my_list)
for i in range(l):
    print(str(i+1),(my_list[i][:10]))

my_list = input('Введите несколько слов. Разделите слова пробелами: ')
my_list = my_list.split()
print(type(my_list))
for num, val in enumerate(my_list, 1):
    print(str(num) + str(val[:10]))







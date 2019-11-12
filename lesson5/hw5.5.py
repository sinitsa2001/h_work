#Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from random import randint

with open('text_5.5.txt', 'w') as f:

    my_list = [randint(1,5) for el in range(5)]
    print(my_list)
    for i in my_list:
        m_list = int(sum(my_list))
    print(m_list)
    symm = str(m_list)
    m_str = str(my_list).split(',')
    f.write(f'А вот и список: {m_str} и его сумма: {symm}')






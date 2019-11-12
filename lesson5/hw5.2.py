# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
# часть первая = считаем строки
from collections import Counter
from functools import reduce
import collections



with open(r'text_5.2.txt', 'r')as f:
        f_lines = f.readlines()
        for  i in f_lines:
            print(f'Слова в строке в кол-ве: {len(i.split())}')
        print(f' Количество строк в файле: {len(f_lines)} шт')



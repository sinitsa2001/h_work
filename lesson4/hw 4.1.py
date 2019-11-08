#Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv
salary_func,rate_param, prod_param, award_param = argv


print('Ставка в час: ', rate_param, 'недооцененок')
print('Выработка: ', prod_param, 'пота и крови')
print('Премия: ', award_param, 'надежд и ожиданий')

x = int(rate_param)
y = int(prod_param)
z = int(award_param)
#m_data = [rate_param,prod_param,award_param]

def salary_func(x,y,z):
    salary = (x * y+z)
    return salary
print(f'Выплата с учетом выработки и ставки +премия: '  , salary_func(x,y,z), 'малоденег')



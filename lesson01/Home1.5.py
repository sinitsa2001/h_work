#5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль
# фирмы в расчете на одного сотрудника.
revenue = int(input('Введите выручку предприятия: '))
cost = int(input('Введите издержки предприятия: '))

if revenue > cost:
    print('Предприятие прибыльно')
    staff = int(input('Сколько людей работает на предприятии: '))
    profit = revenue - cost
    prodact = ('{:.2f}'.format(profit / staff))
    print(f'Рентабельность предриятия равна: {prodact} %')
else:
    print('Предприятие убыточно')

#вариант2
revenue = int(input('Введите выручку предприятия: '))
cost = int(input('Введите издержки предприятия: '))
profit = revenue - cost
if profit >0:
    print('Предприятие прибыльно!')
    staff = int(input('Сколько людей работает на предприятии: '))
    prodact = ('{:.2f}'.format(profit / staff))
    print (f'Рентабельность предриятия равна: {prodact} %')
else:
    print('Предприятие убыточно')



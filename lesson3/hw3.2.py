#Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.



def data_func(var_name, var_surname, var_place, var_mail, var_phone):
    print(f'{var_name} {var_surname}; город: {var_place}; e-mail:{var_mail}; tel:{var_phone}')
name = input('Введите ваше ваше имя: ')
surname = input('Введите вашу фамилию: ')
place = input('Введите ваше место проживания: ')
mail = input('Введите ваш email: ')
phone = input('Введите номер вашего телефона: ')
data_func(name,surname,place,mail,phone)






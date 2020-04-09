#2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

user_time = int(input("Введите время в секундах: "))
hour = str(user_time//3600)
minute = (user_time//60)%60
second = user_time % 60
if minute<10:
    minute = ("0"+ str(minute))
    #print(minute)
else:
    minute = str(minute)
    #print(minute)
if second < 10:
    second = ("0" + str(second))
    #print(second)
else:
    second = (str(second))
print(f'Ваше время: {hour}:{minute}:{second}')

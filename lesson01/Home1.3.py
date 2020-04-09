#3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
number = int(input('Введите число от 0 до 10: '))
param1 = int(str(number)+ str(number))
param2 = int(str(param1) + str(number))
result = number+param1+param2
print(result)
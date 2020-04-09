#4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
value = int(input('Введите число:  '))
result = value%10
value = value//10
while value > 0:
    if value%10 > result:
        result = value%10
    value = value//10
print(f'Самая большая цифра в числе: {result}')
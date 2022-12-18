# Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

number = float(input('Введите число -> '))
sum = 0
if number < 0:
    number *= -1
while number != int(number):
    number = round(number * 10, 10)
while number > 0:
    digit = number % 10
    sum = sum + digit
    number = number // 10
print (f'Сумма цифр числа равна: {sum}')

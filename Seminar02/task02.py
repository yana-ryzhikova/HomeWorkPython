# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел 
# от 1 до N.
# *Пример:*

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# number = int(input('Введите число N -> '))
# factorial = 1
# i = 1
# while i <= number:
#     factorial = i * factorial
#     print(factorial)
#     i += 1

number = int(input('Введите число N -> '))
factorial = 1
i = 1
if number > 0:
    while i <= number:
        factorial = i * factorial
        print(factorial)
        i += 1
else:
    print('Невозможно вычислить факториал. Введите число больше 0.')
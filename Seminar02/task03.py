# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и 
# выведите на экран их сумму.
# *Пример:*

# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# n = int(input('Введите число N -> '))
# my_list = []
# for i in range(1, n + 1):
#     my_list[i] = round((1 + 1 / i), 3)
# print(my_list)

# n = int(input('Введите число N -> '))        +++
# my_list = [round((1+1/i)**i, 3) for i in range(1, n+1)]
# sum = round(sum(my_list), 3)
# print(f'{my_list} {sum}')

n = int(input('Введите число N -> '))
my_list = []
for i in range(1, n+1):
    my_list.append(round((1+1/i)**i, 3))
print(f'Список: {my_list}')
sum = round(sum(my_list), 3)
print(f'Сумма: {sum}')


# Реализуйте алгоритм перемешивания списка.

n = int(input('Введите число N -> '))
my_list = []
for i in range(0, n):
    my_list.append(input('Введите элемент списка: '))
print(f'Список до перемешивания: {my_list}')
import random
random.shuffle(my_list)
print(f'Список после перемешивания: {my_list}')
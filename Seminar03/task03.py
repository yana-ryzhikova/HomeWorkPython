# 3. Задайте список из вещественных чисел. Напишите программу, которая 
# найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19



import random
len_list  = int(input('Введите длину списка: '))
my_list = []
for i in range(len_list):
    i = round(random.uniform(1, 15), 2)
    my_list.append(i)
print(f'Исходный список: {my_list}')

new_list = []
for i in my_list:
    i = round((i - int(i)), 2)
    new_list.append(i)
#print(new_list)

diff = round(max(new_list) - min(new_list), 2)
print(f'Разница между макс и мин значением дробной части элементов -> {diff}')
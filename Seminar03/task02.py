# 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

my_list = [2, 3, 4, 5, 6]
print(f'Исходный список: {my_list}')
multiplication = 0
new_list = []
if len(my_list) % 2 != 0:
    for i in range(0, int(len(my_list)/2 + 1)):
        new_list.append(my_list[i] * my_list[len(my_list)-i-1])
else:
    for i in range(0, int(len(my_list)/2)):
        new_list.append(my_list[i] * my_list[len(my_list)-i-1])
print(f'Cписок произведений элементов: {new_list}')
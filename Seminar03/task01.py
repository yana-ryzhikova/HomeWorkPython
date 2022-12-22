# 1. Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# my_list = [2, 3, 5, 9, 3]
# print(f'{my_list}')
# sum = 0
# for i in range(0, len(my_list)):
#     if i % 2 != 0:
#         sum += my_list[i]
# print(f'Сумма элементов списка на нечетных позициях -> {sum}')

my_list = [2, 3, 5, 9, 3]
print(f'{my_list}')
def Sum_Odd(my_list, sum):
    sum = 0
    for i in range(0, len(my_list)):
        if i % 2 != 0:
            sum += my_list[i]
    return sum
print(f'Сумма элементов списка на нечетных позициях -> {Sum_Odd(my_list, sum)}')
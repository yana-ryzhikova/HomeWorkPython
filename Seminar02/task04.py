# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.


n = int(input('Введите число N: '))
my_list = []
for i in range(-n, n + 1):
    my_list.append(i)
print(my_list)

a = int(input('Введите позицию 1: '))
b = int(input('Введите позицию 2: '))
c = int(input('Введите позицию 3: '))
for i in my_list:
    mult = my_list[a] * my_list[b] * my_list[c]
print(f'Произведение элементов на указанных позициях: {mult}')

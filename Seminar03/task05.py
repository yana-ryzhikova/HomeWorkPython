# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример:*

# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

num = int(input('Введите число: '))

tmp1 = 0
tmp2 = 1
f_pos = []
f_pos.append(tmp1)
f_pos.append(tmp2)
for i in range(2, num + 1):
        i = tmp1 + tmp2
        tmp1 = tmp2
        tmp2 = i
        f_pos.append(i)
#print(f_pos)


tmp1 = 0
tmp2 = 1
f = []
f.append(tmp2)
for i in range(2, num + 1):
        i = tmp1 - tmp2
        tmp1 = tmp2
        tmp2 = i
        f.insert(0, i)
#print(f)

nf = f + f_pos
print(f'Список чисел Фибоначчи, в том числе для отрицательных индексов, для числа {num} ->')
print(nf)
# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num  = int(input('Введите число: '))
print(f'Преобразованное из десятичного в двоичное число {num} ->')
binary = []
while num != 0:
    if num % 2 != 0:
        x = 1
        num = num // 2
    else:
        num % 2 == 0
        x = 0
        num = num // 2
    binary.append(str(x))
print(''.join(reversed(binary)))


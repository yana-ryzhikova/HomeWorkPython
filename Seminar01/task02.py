# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.

for x in True, False:
    for y in True, False:
        for z in True, False:
            print(x, y, z, end=' -> ')
            print(not (x and y and z) == (not x) or (not y) or (not z))

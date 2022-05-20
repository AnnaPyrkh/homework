# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

import random

r = [random.randint(-10, 2) for i in range(12)]
print(f'Список: {r}')

min_index = 0

for i in r:
    if r[min_index] > i:
        min_index = r.index(i)

if r[min_index] >= 0:
    print(f'В списке нет отрицательных элементов')
else:
    print(f'В списке минимальный отрицательный элемент: {r[min_index]}.',
          f'Находится на позиции {min_index}')

"""
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках
первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным
использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной
и той же задачи. Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.
"""
# Python 3.8 (32-bit)
# Тест выполнен на 64-разрядной Win 10
# Урок 3, задание 9

# 1 вариант

import random
import sys

matrix = []

for i in range(5):
    matrix.append([])
    matrix[i].extend([random.randint(1, 10) for _ in range(5)])

min_list = []
min_list.extend(matrix[0])

for string in matrix:
    print()
    print(('{:4d} ' * len(string)).format(*string))
    i = 0
    for j in string:
        if j < min_list[i]:
            min_list[i] = j
        i += 1

print()
print('min_list')
print(('{:4d} ' * len(min_list)).format(*min_list))
print()

min_list.sort(reverse=True)
print(
    'Максимальный элемент среди минимальных элементов столбцов матрицы: ',
    min_list[0]
)

sum_size = 0
sum_size += sys.getsizeof(matrix)
sum_size += sys.getsizeof(min_list)
sum_size += sys.getsizeof(i)
sum_size += sys.getsizeof(string)
sum_size += sys.getsizeof(j)

print('Переменные занимают', sum_size)


# Размер переменных в текущем случае - 208.


# 2 вариант

def show_size(x, level=0):
    print('\t' * level, f'type = {x.__class__}, size = {sys.getsizeof(x)}, object = {x}')

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for y in x.items():
                show_size(y, level + 1)

        elif not isinstance(x, str):
            for y in x:
                show_size(y, level + 1)


def matrix_func(matrix):
    for i, line in enumerate(matrix):

        if i == 0:
            min_line = line.copy()
            continue

        for idx, item in enumerate(line):
            if item < min_line[idx]:
                min_line[idx] = item

    max_min = min_line[0]
    for item in min_line:
        if item > max_min:
            max_min = item
    return locals()


lst = [random.randint(-20, 0) for _ in range(20)]

matrix = [[1, 2, 7], [4, 1, 5], [5, 6, 3]]
show_size(matrix_func(matrix))

"""
type = <class 'dict'>, size = 196, object = {'matrix': [[1, 2, 7], [4, 1, 5], [5, 6, 3]], 
'i': 2, 'line': [5, 6, 3], 'min_line': [1, 1, 3], 'idx': 2, 'item': 3, 'max_min': 3}
	 type = <class 'tuple'>, size = 28, object = ('matrix', [[1, 2, 7], [4, 1, 5], [5, 6, 3]])
		 type = <class 'str'>, size = 31, object = matrix
		 type = <class 'list'>, size = 40, object = [[1, 2, 7], [4, 1, 5], [5, 6, 3]]
			 type = <class 'list'>, size = 40, object = [1, 2, 7]
				 type = <class 'int'>, size = 14, object = 1
				 type = <class 'int'>, size = 14, object = 2
				 type = <class 'int'>, size = 14, object = 7
			 type = <class 'list'>, size = 40, object = [4, 1, 5]
				 type = <class 'int'>, size = 14, object = 4
				 type = <class 'int'>, size = 14, object = 1
				 type = <class 'int'>, size = 14, object = 5
			 type = <class 'list'>, size = 40, object = [5, 6, 3]
				 type = <class 'int'>, size = 14, object = 5
				 type = <class 'int'>, size = 14, object = 6
				 type = <class 'int'>, size = 14, object = 3
	 type = <class 'tuple'>, size = 28, object = ('i', 2)
		 type = <class 'str'>, size = 26, object = i
		 type = <class 'int'>, size = 14, object = 2
	 type = <class 'tuple'>, size = 28, object = ('line', [5, 6, 3])
		 type = <class 'str'>, size = 29, object = line
		 type = <class 'list'>, size = 40, object = [5, 6, 3]
			 type = <class 'int'>, size = 14, object = 5
			 type = <class 'int'>, size = 14, object = 6
			 type = <class 'int'>, size = 14, object = 3
	 type = <class 'tuple'>, size = 28, object = ('min_line', [1, 1, 3])
		 type = <class 'str'>, size = 33, object = min_line
		 type = <class 'list'>, size = 40, object = [1, 1, 3]
			 type = <class 'int'>, size = 14, object = 1
			 type = <class 'int'>, size = 14, object = 1
			 type = <class 'int'>, size = 14, object = 3
	 type = <class 'tuple'>, size = 28, object = ('idx', 2)
		 type = <class 'str'>, size = 28, object = idx
		 type = <class 'int'>, size = 14, object = 2
	 type = <class 'tuple'>, size = 28, object = ('item', 3)
		 type = <class 'str'>, size = 29, object = item
		 type = <class 'int'>, size = 14, object = 3
	 type = <class 'tuple'>, size = 28, object = ('max_min', 3)
		 type = <class 'str'>, size = 32, object = max_min
		 type = <class 'int'>, size = 14, object = 3
"""

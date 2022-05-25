"""Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Урок 3, задание 9 - найти максимальный элемент среди минимальных элементов столбцов матрицы
"""


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
            assert isinstance(item)
            max_min = item


def matrix_func2(matrix):

    max_ = float('-inf')

    for j in range(len(matrix[0])):
        min_ = matrix[0][j]

        for i in range(len(matrix)):
            if matrix[i][j] < min_:
                min_ = matrix[i][j]

        if min_ > max_:
            max_ = min_

# python -m timeit -n 100 -s "import random"
# "x = [[random.randint(1, 10) for _ in range(3)] for _ in range(3)]"
# 100 loops, best of 5: 9.65 usec per loop  (3x3)
# 100 loops, best of 5: 79.2 usec per loop (3x3)

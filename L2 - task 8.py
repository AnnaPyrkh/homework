"""
8. Посчитать, сколько раз встречается определенная цифра в введенной
последовательности чисел. Количество вводимых чисел и цифра, которую необходимо
посчитать, задаются вводом с клавиатуры.
"""


user_range = input('Введите последовательность: ')
user_patten = input('Введите цифру для поиска: ')
count = 0

for i in user_range:
    if i == user_patten:
        count += 1

print(f'Цифра встречается {user_patten} в последовательности {user_range}: \
{count} раз(а)')

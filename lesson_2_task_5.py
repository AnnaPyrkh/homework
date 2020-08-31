positive_integer = [8, 6, 5, 5, 4]
print(f'Рейтинг - {positive_integer}')
digit = int(input('Введите простое число. Если хотите выйти, введите 1000: '))
while digit != 1000:
    for el in range(len(positive_integer)):
        if positive_integer[el] == digit:
            positive_integer.insert(el + 1, digit)
            break
        elif positive_integer[0] < digit:
            positive_integer.insert(0, digit)
        elif positive_integer[-1] > digit:
            positive_integer.append(digit)
        elif positive_integer[el] > digit > positive_integer[el + 1]:
            positive_integer.insert(el + 1, digit)
    print(f'Текущий список: {positive_integer}')
    digit = int(input('Введите следующее число: '))

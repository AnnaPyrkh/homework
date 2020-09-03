# вариант 1
def my_func(x, y):
    result = 1
    for i in range(abs(y)):
        result *= x
    if y >= 0:
        return result
    else:
        return 1 / result


print(my_func(float(input('Введите значения для х: ')), int(input('Введите значение для у: '))))

# вариант 2


def my_func(x, y):
    return 1 / x ** abs(y)


print(my_func(float(input('Введите значения для х: ')), int(input('Введите значение для у: '))))

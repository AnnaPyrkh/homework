def divide(*args):

    try:
        num1 = int(input('Введите первое число: '))
        num2 = int(input('Введите второе число: '))
        result = round(num1 / num2, 2)
    except ValueError:
        return 'Ошибка: введённое значение не является числом!'
    except ZeroDivisionError:
        return "Ошибка: деление на 0!"

    return result


print(f'Результат: {divide()}')

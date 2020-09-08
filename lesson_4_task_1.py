from sys import argv

name, time, salary, bonus = argv

try:
    time = int(time)
    salary = int(salary)
    bonus = int(bonus)
    res = time * salary + bonus
    print(f'заработная плата сотрудника  {res}')
except ValueError:
    print('')


def sal():
    try:
        hours = float(input('Отработано часов: '))
        wage = int(input('Ставка в час: '))
        prize = int(input('Премия: '))
        result = hours * wage + prize
        print(f'Заработная плата сотрудника:  {result}')
    except ValueError:
        return print('Not a number')


sal()

revenue = int(input('Введите выручку фирмы: '))
expenses = int(input('Введите расходы фирмы: '))

if revenue > expenses:
    print(f'Фирма приносит прибыль в размере: {revenue - expenses} денег')
    staff = int(input('Введите количество персонала фирмы: '))
    print(f'Прибыль в расчете на одного сторудника сотавила: {revenue/ staff} денег')
elif revenue == expenses:
    print('Фирма вышла на самоокупаемость, но прибыль пока не приносит')
else:
    print('Фирма работает в минус :(')

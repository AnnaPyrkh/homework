user_name = input('Введите ваше имя: ')
user_age = int(input('Введите ваш возраст: '))
user_address = input('Введите ваш адрес: ')
print(f'Имя: {user_name}, Возраст: {user_age}, Адрес: {user_address}')



time = int(input('Введите время в секундах: '))
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time - (hours * 3600 + minutes * 60)
print(f'Время в формате "чч:мм:сс":  {hours} : {minutes} : {seconds}')



user_number = int(input('Введите число n: '))

number = str(user_number)
double_number = number + number
triple_number = number + number + number
result = user_number + int(double_number) + int(triple_number)

print('Итог:', result)



user_number = int(input('Введите любое положительное число: '))
gross = user_number % 10

while user_number >= 1:
    user_number = user_number // 10
    if user_number % 10 > gross:
        gross = user_number % 10
    if user_number > 9:
        continue

    else:
        print('Самая большая цифра в числе: ', gross)

        break
        
        

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
    
    
    
first_day_km = int(input('Сколько км вам удалось преодолеть в первый день? : '))
goal_km = int(input('Укажите вашу цель по км в день: '))
result_days = 1


while goal_km - first_day_km > 0:
    first_day_km = first_day_km + (first_day_km * 0.1)
    result_days += 1

print(f'Вы осилите целевые показатели на %.d день' % result_days)
© 2020 GitHub, Inc.

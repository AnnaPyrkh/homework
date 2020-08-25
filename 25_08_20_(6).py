first_day_km = int(input('Сколько км вам удалось преодолеть в первый день? : '))
goal_km = int(input('Укажите вашу цель по км в день: '))
result_days = 1


while goal_km - first_day_km > 0:
    first_day_km = first_day_km + (first_day_km * 0.1)
    result_days += 1

print(f'Вы осилите целевые показатели на %.d день' % result_days)
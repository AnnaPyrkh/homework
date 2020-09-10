import json
profit = {}
income = {}
margin = 0
prof_average = 0
i = 0
with open('task_7_firms.txt') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            margin = margin + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_average = margin / i
        print(f'Прибыль средняя: {prof_average:.2f}')
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    income = {'Средняя прибыль': round(prof_average)}
    profit.update(income)
    print(f'Прибыль каждой компании: {profit}')

with open('task_7_firms.json', 'w') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f'Создан файл с расширением .json со следующим содержимым:\n '
          f' {js_str}')

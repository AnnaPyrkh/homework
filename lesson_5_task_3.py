with open('task_3_salary.txt') as my_f:
    average = []
    misfits = []
    my_list = my_f.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
            misfits.append(i[0])
        average.append(i[1])
        print(f'Оклад меньше 20.000 у: {misfits}; средний оклад: {sum(map(int, average)) / len(average)}')

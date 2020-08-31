goods = []
parameters = {'Название': '', 'Цена': '', 'Количество': '', 'Единица измерения': ''}
analytics = {'Название': [], 'Цена': [], 'Количество': [], 'Единица измерения': []}
num = 0
feature = None
control = None
while True:
    control = input('Для выхода нажмите "Q", чтобы продолжить - "Enter". Получить аналитику - "A": ').upper()
    if control == 'Q':
        break
    num += 1
    if control == 'A':
        print(f'\n Текущая аналитика\n{"-" * 30}')
        for key, value in analytics.items():
            print(f'{key[:25]:>30}: {value}')
            print("-" * 30)
    for f in parameters.keys():
        feature = input(f'Введите характеристику "{f}": ')
        parameters[f] = int(feature) if (f == 'Цена' or f == 'Количество') else feature
        analytics[f].append(parameters[f])
    goods.append((num, parameters))


goods = int(input('Введите количество товара: '))
temp = 1
my_dict = []
my_list = []
my_analytics = {}
while temp <= goods:
    my_dict = dict({'Название': input('Введите название: '), 'Цена': input('Введите цену: '),
                    'Количество': input('Введите количество: '), 'Единица измерения': input('Введите ЕИ: ')})
    my_list.append((temp, my_dict))
    temp += 1
    my_analytics = dict(
        {'Название': my_dict.get('Название'), 'Цена': my_dict.get('Цена'), 'Количество': my_dict.get('Количество'),
         'Единица измерения': my_dict.get('Единица измерения')})
print(my_list)
print(my_analytics)

elements = int(input('Введите количество элементов списка: '))
elements_list = []
i = 0
el = 0
while i < elements:
    elements_list.append(input('Введите значение элементов списка: '))
    i += 1

for elem in range(int(len(elements_list) / 2)):
    elements_list[el], elements_list[el + 1] = elements_list[el + 1], elements_list[el]
    el += 2
print(elements_list)

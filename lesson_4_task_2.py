my_list = [8, 11, 11, 23, 9, 6, 4, 100]
my_new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(f'Исходный список: {my_list}')
print(f'Новый список: {my_new_list}')

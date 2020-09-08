my_list = [2, 5, 6, 1, 4, 4, 9, 10, 7, 5]
my_new_list = [num for num in my_list if my_list.count(num) < 2]
print(my_new_list)

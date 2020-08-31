my_list = ['hello', True, 8, -11, 2.5, None, {'age: 29, sex: female'}, [2, 3, 5], (1, 6)]


def show_type(i):

    for i in range(len(my_list)):
        print(type(my_list[i]))
    return


show_type(my_list)
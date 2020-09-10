def summary():
    try:
        with open('task_5_summary.txt', 'w+') as file_obj:
            line = input('Введите числа через пробел: \n')
            file_obj.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка ввода-вывода!')
    except ValueError:
        print('Введенное значение не является числом!')


summary()

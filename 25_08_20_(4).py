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



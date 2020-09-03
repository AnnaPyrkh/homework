def my_sum():
    sum_result = 0
    temp = False
    while not temp:
        numbers = input('Введите число или Q для выхода: ').split()
        result = 0
        for i in range(len(numbers)):
            if numbers[i] == 'q' or numbers[i] == 'Q':
                temp = True
                break
            else:
                result = result + int(numbers[i])
        sum_result = sum_result + result
        print(f'Текущая сумма: {sum_result}')
    print(f'Финальная сумма: {sum_result}')


my_sum()

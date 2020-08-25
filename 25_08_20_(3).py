user_number = int(input('Введите число n: '))

number = str(user_number)
double_number = number + number
triple_number = number + number + number
result = user_number + int(double_number) + int(triple_number)

print('Итог:', result)

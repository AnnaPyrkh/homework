# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь

number = input('Введите трехзначное число: ')

amount = 0
prod = 1

for i in number:
    amount += int(i)
    prod *= int(i)
print(f'Сумма цифр числа {number}: {amount}')
print(f'Произведение цифр: {number}: {prod}')

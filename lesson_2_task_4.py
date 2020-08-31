user_str = input('Введите несколько слов через пробел: ')
words = []
string_number = 1
for i in range(user_str.count(' ') + 1):
    words = user_str.split()
    if len(str(words)) <= 10:
        print(f'{string_number} {words [i]}')
        string_number += 1
    else:
        print(f'{string_number} {words [i] [0:10]}')
        string_number += 1

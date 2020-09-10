file_name = input('Введите название и формат файла: ')
f = open(file_name, 'w')
while True:
    string = input()
    if string == '':
        break
    f.write(string + '\n')
f.close()

with open('task_2_count_elements.txt') as f:
    string = 0
    for i in f:
        string += 1

        symbol = 0
        word = 0
        for j in i:
            if j != ' ' and symbol == 0:
                word += 1
                symbol = 1
            elif j == ' ':
                symbol = 0

        print(i, len(i), 'симв.', word, 'слов')

    print(string, 'строк всего')
    f.close()

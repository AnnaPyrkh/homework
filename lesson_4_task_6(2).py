from itertools import cycle

my_list = [False, 'what a wonder', 999, (2, 4, 6), True]
for el in cycle(my_list):
    print(el)

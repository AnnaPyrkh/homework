from itertools import count
from math import factorial


def factor():
    for el in count(1):
        yield factorial(el)


generator = factor()
x = 0
for i in generator:
    if x < 20:
        print(i)
        x += 1
    else:
        break

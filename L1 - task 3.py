# По введенным пользователем координатам двух точек вывести уравнение
# прямой вида y=kx+b, проходящей через эти точки

x1, y1, x2, y2 = [
    int(x) for x in input('Введите кординаты (x1, y1, x2, y2): ').split()
]

k = (y2 - y1)/(x2 - x1)
b = y1 - k * x1

print(f'Уравнение прямой: y = {k}x + {b}')


def my_func(a, b, c):
    z = [a, b, c]
    z.remove(min(a, b, c))
    return sum(z)


print(f'Результат = {my_func(int(input("Число 1: ")), int(input("Число 2: ")), int(input("Число 3: ")))}')

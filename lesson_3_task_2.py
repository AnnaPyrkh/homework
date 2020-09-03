name = input('Введите ваше имя: ')
surname = input('Введите вашу фамилию: ')
birth_year = int(input('Введите ваш год рождения: '))
location = input('Введите ваш город: ')
email = input('Введите ваш e-mail: ')
telephone = int(input('Введите ваш номер телефона: '))


def my_func(**kwargs):
    return [name, surname, birth_year, location, email, telephone]


print(my_func())

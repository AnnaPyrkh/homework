class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # methods
    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def show_speed(self):
        return f'Текущая скорость {self.name} : {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость TownCar {self.name} : {self.speed}')

        if self.speed > 40:
            return f'Скорость {self.name} выше допустимой нормы для TownCar'
        else:
            return f'Скорость {self.name} в пределах нормы для TownCar'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость WorkCar {self.name} : {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.name} выше допустимой нормы для WorkCar'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} из полицеского кортежа'
        else:
            return f'{self.name} не из полицеского кортежа'


aston_martin = SportCar(100, 'Black', 'Aston Martin', False)
volkswagen = TownCar(30, 'Grey', 'Volkswagen', False)
dodge = WorkCar(70, 'Red', 'Dodge', True)
lada = PoliceCar(110, 'White', 'Lada', True)
print(dodge.turn_left())
print(f'Если {volkswagen.turn_right()}, то {aston_martin.stop()}')
print(f'{dodge.go()} со скоростью: {dodge.show_speed()}')
print(f'{dodge.name} is {dodge.color}')
print(f'Является ли {aston_martin.name} полицеской машиной? {aston_martin.is_police}')
print(f'Является ли {dodge.name}  полицейской машиной? {dodge.is_police}')
print(aston_martin.show_speed())
print(volkswagen.show_speed())
print(lada.police())
print(lada.show_speed())

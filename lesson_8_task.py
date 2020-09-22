from random import randint
import random


def generate_unique_numbers(count, min_inbound, max_inbound):
    if count > max_inbound - min_inbound + 1:
        raise ValueError('Некорректные входящие данные!')
    ret = []
    while len(ret) < count:
        new = randint(min_inbound, max_inbound)
        if new not in ret:
            ret.append(new)
    return ret


class Keg:
    __num = None

    def __init__(self):
        self.__num = random.randint(1, 90)
        self.__num = randint(1, 90)

    @property
    def num(self):
        return self.__num

    def __str__(self):
        return str(self.__num)


class Card:
    pass
    __rows = 3
    __cols = 9
    __nums_in_row = 5
    __data = None
    __empty_number = 0
    __cross_end_num = -1

    def __init__(self):
        uniques_count = self.__nums_in_row * self.__rows
        uniques = generate_unique_numbers(uniques_count, 1, 90)

        self.__data = []
        for i in range(0, self.__rows):
            tmp = sorted(uniques[self.__nums_in_row * i: self.__nums_in_row * (i + 1)])
            empty_nums_count = self.__cols - self.__nums_in_row
            for j in range(0, empty_nums_count):
                index = randint(0, len(tmp))
                tmp.insert(index, self.__empty_number)
            self.__data += tmp

    def __str__(self):
        delimiter = '--------------------------'
        ret = delimiter + '\n'
        for index, num in enumerate(self.__data):
            if num == self.__empty_number:
                ret += '  '
            elif num == self.__cross_end_num:
                ret += ' -'
            elif num < 10:
                ret += f' {str(num)}'
            else:
                ret += str(num)

            if (index + 1) % self.__cols == 0:
                ret += '\n'
            else:
                ret += ' '

        return ret + delimiter

    def __contains__(self, item):
        return item in self.__data

    def cross_num(self, num):
        for index, item in enumerate(self.__data):
            if item == num:
                self.__data[index] = self.__cross_end_num
                return
        raise ValueError(f'Number not in card: {num}')

    def closed(self) -> bool:
        return set(self.__data) == {self.__empty_number, self.__cross_end_num}


class Game:
    __user_card = None
    __computer_card = None
    __quantity_kegs = 90
    __kegs = []
    __game_over = False

    def __init__(self):
        self.__user_card = Card()
        self.__computer_card = Card()
        self.__kegs = generate_unique_numbers(self.__quantity_kegs, 1, 90)

    def play_round(self) -> int:
        """
        :return:
        0 - game must go on
        1 - user wins
        2 - computer wins
        """

        keg = self.__kegs.pop()
        print(f'Новый бочонок: {keg} (осталось {len(self.__kegs)})')
        print(f'----- Ваша карточка ------\n{self.__user_card}')
        print(f'-- Карточка компьютера ---\n{self.__computer_card}')

        user_answer = input('Зачеркнуть цифру? (y/n): ').lower().strip()
        if user_answer == 'y' and keg not in self.__user_card or \
                user_answer != 'y' and keg in self.__user_card:
            return 2

        if keg in self.__user_card:
            self.__user_card.cross_num(keg)
            if self.__user_card.closed():
                return 1
        if keg in self.__computer_card:
            self.__computer_card.cross_num(keg)
            if self.__computer_card.closed():
                return 2

        return 0


game = Game()
while True:
    score = game.play_round()
    if score == 1:
        print('Вы выиграли!')
        break
    elif score == 2:
        print('Вы проиграли!')
        break

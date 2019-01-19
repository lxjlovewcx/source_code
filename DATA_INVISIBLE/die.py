from random import randint
class Die():
    """"""

    def __init__(self, side_numbers=6):  #接受一个可选的参数

        self.side_numbers = side_numbers


    def roll(self):
        return randint(1, self.side_numbers)
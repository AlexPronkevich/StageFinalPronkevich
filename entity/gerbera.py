# Version 1.0
# Author: Pronkevich Alexandra
# Group: QA2022
# Date: 28.05.2023


from entity.flower import Flower


class Gerbera(Flower):
    def __init__(self, color='white', weight=1, price=0):
        super().__init__(weight, price)
        self.__color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    def __str__(self):
        return (f"Gerbera: color = {self.__color}, "
                f"weight = {self.weight} gr, "
                f"price = {self.price} BYN")

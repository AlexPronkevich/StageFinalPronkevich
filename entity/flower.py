# Version 1.0
# Author: Pronkevich Alexandra
# Group: QA2022
# Date: 28.05.2023


class Flower:
    def __init__(self, weight=1, price=0):
        self.__weight = weight
        self.__price = price


    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        if isinstance(weight, (int, float)) and weight > 0:
            self.__weight = weight

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if isinstance(price, (int, float)) and price > 0:
            self.__price = price

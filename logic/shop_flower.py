# Version 1.0
# Author: Pronkevich Alexandra
# Group: QA2022
# Date: 28.05.2023


from container.bouquet import Bouquet
from entity.flower import Flower


class ShopFlower:
    @staticmethod
    def calculate_total_weight(bouquet):
        if isinstance(bouquet, Bouquet) and bouquet.size != 0:
            total_weight = 0
            for i in range(bouquet.size):
                flower = bouquet.get_flower(i)

                if isinstance(flower, Flower):
                    total_weight += flower.weight

            return total_weight
        else:
            return 0

    @staticmethod
    def calculate_total_price(bouquet):
        if isinstance(bouquet, Bouquet) and bouquet.size != 0:
            total_price = 0
            for i in range(bouquet.size):
                flower = bouquet.get_flower(i)

                if isinstance(flower, Flower):
                    total_price += flower.price

            return total_price
        else:
            return 0

    # def get_max_price(bouquet):
    #     max_price = max(bouquet)
    #     return max_price
    # 
    # def get_min_price(bouquet):
    #     min_price = min(bouquet)
    #     return min_price


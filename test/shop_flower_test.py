# Version 1.0
# Author: Pronkevich Alexandra
# Group: QA2022
# Date: 03.06.2023

import unittest

from container.bouquet import Bouquet
from entity.flower import Flower
from logic.shop_flower import ShopFlower


class ShopFlowerTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.shop_fl = ShopFlower()

    @classmethod
    def tearDownClass(cls):
        del cls.shop_fl

    def test_different_type(self):
        bouquet = "string"
        expected = 0

        actual = ShopFlower.calculate_total_price(bouquet)

        self.assertEqual(expected, actual)

    def test_empty_type(self):
        bouquet = Bouquet()
        expected = 0

        actual = ShopFlower.calculate_total_price(bouquet)

        self.assertEqual(expected, actual)

    def test_bouquet_with_None(self):
        bouquet = None
        expected = 0

        actual = ShopFlower.calculate_total_price(bouquet)

        self.assertEqual(expected, actual)

    def test_bouquet_with_flowers_positive(self):
        flower1 = Flower(6.5)
        flower2 = Flower(7.5)
        flower3 = Flower(5)

        bouquet = Bouquet()
        bouquet.add(flower1)
        bouquet.add(flower2)
        bouquet.add(flower3)

        expected = 19

        actual = ShopFlower.calculate_total_price(bouquet)

        self.assertEqual(expected, actual)

    def test_flower_with_one_positive(self):
        flower = Flower(5)

        bouquet = Bouquet()
        bouquet.add(flower)

        expected = flower.price

        actual = ShopFlower.calculate_total_price(bouquet)

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

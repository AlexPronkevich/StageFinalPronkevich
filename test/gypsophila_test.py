# Version 1.0
# Author: Pronkevich Alexandra
# Group: QA2022
# Date: 02.06.2023

import unittest
from entity.gypsophila import Gypsophila


class GypsophilaTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.gips = Gypsophila()

    @classmethod
    def tearDownClass(cls):
        del cls.gips

    def test_gypsophila_default_constructor(self):
        rose = Gypsophila()
        expected_color = "white"
        expected_weight = 1
        expected_price = 0

        self.assertEqual(expected_color, gypsophila.color)
        self.assertEqual(expected_weight, gypsophila.weight)
        self.assertEqual(expected_price, gypsophila.price)

    def test_negative_gypsophila_weight(self):
        weight = -20
        expected = 1

        rose = Gypsophila(weight=weight)

        self.assertEqual(expected, gypsophila.weight)

    def test_negative_gypsophila_price(self):
        price = -10
        expected = 0

        rose = Gypsophila(price=price)

        self.assertEqual(expected, gypsophila.price)

    def test_weight_property_positive(self):
        gypsophila = Gypsophila()
        expected = 50
        gypsophila.weight = 50
        self.assertEqual(expected, gypsophila.weight)

    def test_weight_property_zero(self):
        gypsophila = Gypsophila()
        expected = rose.weight
        gypsophila.weight = 0
        self.assertEqual(expected, gypsophila.weight)

    def test_price_property_positive(self):
        gypsophila = Gypsophila()
        expected = 5.5
        gypsophila.price = 5.5
        self.assertEqual(expected, gypsophila.price)


if __name__ == "__main__":
    unittest.main()

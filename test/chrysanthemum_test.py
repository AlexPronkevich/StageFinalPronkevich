# Version 1.0
# Author: Pronkevich Alexandra
# Group: QA2022
# Date: 02.06.2023

import unittest
from entity.chrysanthemum import Chrysanthemum


class ChrysanthemumTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.chrys = Chrysanthemum()

    @classmethod
    def tearDownClass(cls):
        del cls.chrys

    def test_chrysanthemum_default_constructor(self):
        chrysanthemum = Chrysanthemum()
        expected_color = "white"
        expected_weight = 1
        expected_price = 0

        self.assertEqual(expected_color, chrysanthemum.color)
        self.assertEqual(expected_weight, chrysanthemum.weight)
        self.assertEqual(expected_price, chrysanthemum.price)

    def test_negative_chrysanthemum_weight(self):
        weight = -50
        expected = 1

        chrysanthemum = Chrysanthemum(weight=weight)

        self.assertEqual(expected, chrysanthemum.weight)

    def test_negative_chrysanthemum_price(self):
        price = -9
        expected = 0

        chrysanthemum = Chrysanthemum(price=price)

        self.assertEqual(expected, chrysanthemum.price)

    def test_weight_property_positive(self):
        chrysanthemum = Chrysanthemum()
        expected = 25
        chrysanthemum.weight = 25
        self.assertEqual(expected, chrysanthemum.weight)

    def test_weight_property_zero(self):
        chrysanthemum = Chrysanthemum()
        expected = chrysanthemum.weight
        chrysanthemum.weight = 0
        self.assertEqual(expected, chrysanthemum.weight)

    def test_price_property_positive(self):
        chrysanthemum = Chrysanthemum()
        expected = 4.5
        chrysanthemum.price = 4.5
        self.assertEqual(expected, chrysanthemum.price)


if __name__ == "__main__":
    unittest.main()

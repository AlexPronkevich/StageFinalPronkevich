# Version 1.0
# Author: Pronkevich Alexandra
# Group: QA2022
# Date: 02.06.2023

import unittest
from entity.gerbera import Gerbera


class GerberaTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.gerb = Gerbera()

    @classmethod
    def tearDownClass(cls):
        del cls.gerb

    def test_gerbera_default_constructor(self):
        gerbera = Gerbera()
        expected_color = "white"
        expected_weight = 1
        expected_price = 0

        self.assertEqual(expected_color, gerbera.color)
        self.assertEqual(expected_weight, gerbera.weight)
        self.assertEqual(expected_price, gerbera.price)

    def test_negative_gerbera_weight(self):
        weight = -20
        expected = 1

        gerbera = Gerbera(weight=weight)

        self.assertEqual(expected, gerbera.weight)

    def test_negative_gerbera_price(self):
        price = -6
        expected = 0

        gerbera = Rose(price=price)

        self.assertEqual(expected, gerbera.price)

    def test_weight_property_positive(self):
        gerbera = Gerbera()
        expected = 50
        gerbera.weight = 50
        self.assertEqual(expected, gerbera.weight)

    def test_weight_property_zero(self):
        gerbera = Gerbera()
        expected = gerbera.weight
        gerbera.weight = 0
        self.assertEqual(expected, gerbera.weight)

    def test_price_property_positive(self):
        gerbera = Gerbera()
        expected = 5
        gerbera.price = 5
        self.assertEqual(expected, gerbera.price)


if __name__ == "__main__":
    unittest.main()

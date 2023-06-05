# Version 1.0
# Author: Pronkevich Alexandra
# Group: QA2022
# Date: 02.06.2023

import unittest
from entity.alstroemeria import Alstroemeria


class AlstroemeriaTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.alstr = Alstroemeria()

    @classmethod
    def tearDownClass(cls):
        del cls.alstr
        
    def test_alstroemeria_default_constructor(self):
        rose = Alstroemeria()
        expected_color = "white"
        expected_weight = 1
        expected_price = 0

        self.assertEqual(expected_color, alstroemeria.color)
        self.assertEqual(expected_weight, alstroemeria.weight)
        self.assertEqual(expected_price, alstroemeria.price)

    def test_negative_alstroemeria_weight(self):
        weight = -100
        expected = 1

        rose = Alstroemeria(weight=weight)

        self.assertEqual(expected, alstroemeria.weight)

    def test_negative_alstroemeria_price(self):
        price = -6
        expected = 0

        rose = Alstroemeria(price=price)

        self.assertEqual(expected, alstroemeria.price)

    def test_weight_property_positive(self):
        alstroemeria = Alstroemeria()
        expected = 40
        alstroemeria.weight = 40
        self.assertEqual(expected, alstroemeria.weight)

    def test_weight_property_zero(self):
        alstroemeria = Alstroemeria()
        expected = alstroemeria.weight
        alstroemeria.weight = 0
        self.assertEqual(expected, alstroemeria.weight)

    def test_price_property_positive(self):
        alstroemeria = Alstroemeria()
        expected = 7
        alstroemeria.price = 7
        self.assertEqual(expected, alstroemeria.price)


if __name__ == "__main__":
    unittest.main()

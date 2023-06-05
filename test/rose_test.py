# Version 1.0
# Author: Pronkevich Alexandra
# Group: QA2022
# Date: 02.06.2023

import unittest
from entity.rose import Rose


class RoseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.rose = Rose()

    @classmethod
    def tearDownClass(cls):
        del cls.rose

    def test_rose_default_constructor(self):
        rose = Rose()
        expected_color = "white"
        expected_weight = 1
        expected_price = 0

        self.assertEqual(expected_color, rose.color)
        self.assertEqual(expected_weight, rose.weight)
        self.assertEqual(expected_price, rose.price)

    def test_negative_rose_weight(self):
        weight = -20
        expected = 1

        rose = Rose(weight=weight)

        self.assertEqual(expected, rose.weight)

    def test_negative_rose_price(self):
        price = -6
        expected = 0

        rose = Rose(price=price)

        self.assertEqual(expected, rose.price)

    def test_weight_property_positive(self):
        rose = Rose()
        expected = 50
        rose.weight = 50
        self.assertEqual(expected, rose.weight)

    def test_weight_property_zero(self):
        rose = Rose()
        expected = rose.weight
        rose.weight = 0
        self.assertEqual(expected, rose.weight)

    def test_price_property_positive(self):
        rose = Rose()
        expected = 4
        rose.price = 4
        self.assertEqual(expected, rose.price)


if __name__ == "__main__":
    unittest.main()

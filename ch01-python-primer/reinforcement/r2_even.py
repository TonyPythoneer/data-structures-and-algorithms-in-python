#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @first_date  20160728
# @date        20160728
'''R-1.2
Write a short Python function, is even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators.
'''
import unittest


def is_even(num):
    '''is even'''
    odd = 0b01
    return num & odd != odd


class TestIsEven(unittest.TestCase):
    def setUp(self):
        self.func = is_even

    def test_input_odds(self):
        for odd in range(1, 10, 2):
            self.assertFalse(self.func(odd))

    def test_input_evens(self):
        for even in xrange(0, 10, 2):
            self.assertTrue(self.func(even))


if __name__ == '__main__':
    unittest.main()

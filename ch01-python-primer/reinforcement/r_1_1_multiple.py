#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @first_date  20160623
# @date        20160623
'''R-1.1
Write a short Python function, is multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise.
'''
import unittest


def multiple(n, m):
    remainder = n % m
    is_multiple = remainder == 0
    return is_multiple


class TestMutiple(unittest.TestCase):
    def setUp(self):
        self.func = multiple

    def test_dividend_and_divisor_are_same(self):
        dividend, divisor = 10, 10
        self.assertTrue(self.func(dividend, divisor))

    def test_dividend_is_a_mutiple_of_divisor(self):
        dividend, divisor = 20, 10
        self.assertTrue(self.func(dividend, divisor))

    def test_dividend_is_not_a_mutiple_of_divisor(self):
        dividend, divisor = 10, 20
        self.assertFalse(self.func(dividend, divisor))


if __name__ == '__main__':
    unittest.main()

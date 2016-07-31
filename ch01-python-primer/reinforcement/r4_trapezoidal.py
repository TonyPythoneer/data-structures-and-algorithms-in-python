#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @first_date  20160728
# @date        20160728
'''R-1.4
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.
'''
import unittest


def trapezoidal_with_sum(n):
    '''normal algorithm'''
    if n <= 0:
        return 0
    return sum(list(range(n)))


def trapezoidal_with_reduce(n):
    '''better algorithm'''
    if n <= 0:
        return 0
    return reduce(lambda x, y: x + y, range(n))


def trapezoidal_algorithm(n):
    '''the best algorithm'''
    if n <= 0:
        return 0
    upper_limit = n - 1
    return (1 + upper_limit) * upper_limit / 2



class TestNormalAlgorithm(unittest.TestCase):
    def setUp(self):
        self.func = trapezoidal_with_sum

    def test_input_negative_number(self):
        result = self.func(-1)
        self.assertEqual(result, 0)

    def test_input_zero(self):
        result = self.func(0)
        self.assertEqual(result, 0)

    def test_input_positive_number(self):
        result = self.func(5)
        self.assertEqual(result, (1 + 5 - 1) * (5 - 1) / 2)


class TestBetterAlgorithm(TestNormalAlgorithm):
    def setUp(self):
        self.func = trapezoidal_with_reduce


class TestTheBestAlgorithm(TestNormalAlgorithm):
    def setUp(self):
        self.func = trapezoidal_algorithm


if __name__ == '__main__':
    unittest.main()

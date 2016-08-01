#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @first_date  20160801
# @date        20160801
'''R-1.6
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n.
'''
import unittest


def func_with_sum(num):
    return sum(xrange(1, num, 2))


def func_with_reduce(num):
    num = num - 1 if num % 2 == 0 else num
    return reduce(lambda x, y: x + y, xrange(1, num, 2))


class Test(unittest.TestCase):
    def setUp(self):
        self.func = func_with_sum

    def test_input_nine(self):
        func_result, expected_result = self.func(9), sum(xrange(1, 9, 2))
        self.assertEqual(func_result, expected_result)

    def test_input_ten(self):
        func_result, expected_result = self.func(10), sum(xrange(1, 10, 2))
        self.assertEqual(func_result, expected_result)


if __name__ == '__main__':
    unittest.main()

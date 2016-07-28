#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @first_date  20160728
# @date        20160728
'''R-1.3
Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution.
'''
import unittest


def minmax(data):
    '''minmax'''
    length = len(data)
    for i in xrange(length-1):
        for j in xrange(i, length):
            if data[i] > data[j]:
                data[j], data[i] = data[i], data[j]
    return data[0], data[-1]


class TestMinmax(unittest.TestCase):
    def setUp(self):
        self.func = minmax

    def test_input_array_with_one_number(self):
        min_, max_ = self.func([0])
        self.assertEqual(min_, 0)
        self.assertEqual(max_, 0)

    def test_input_array_with_many_number(self):
        data = [1, -7, 7, -9, 5, -3]
        min_, max_ = self.func(data)
        self.assertEqual(min_, min(data))
        self.assertEqual(max_, max(data))


if __name__ == '__main__':
    unittest.main()

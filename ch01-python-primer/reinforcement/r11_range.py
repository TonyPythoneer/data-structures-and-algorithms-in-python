#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @first_date  20160804
# @date        20160804
'''R-1.11
Demonstrate how to use Python’s list comprehension syntax
to produce the list [1, 2, 4, 8, 16, 32, 64, 128, 256].

list_ = []
for i in xrange(9):
    list_.append(2 ** i)
'''
import unittest


def func():
    return [2 ** i for i in xrange(9)]


class Test(unittest.TestCase):
    def setUp(self):
        self.func = func

    def test_first_case(self):
        expect_result = [1, 2, 4, 8, 16, 32, 64, 128, 256]
        self.assertEqual(expect_result, self.func())


if __name__ == '__main__':
    unittest.main()

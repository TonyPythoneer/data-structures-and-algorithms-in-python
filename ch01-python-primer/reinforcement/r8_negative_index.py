#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @first_date  20160801
# @date        20160801
'''R-1.8
Python allows negative integers to be used as indices into a sequence, such as
a string. If string s has length n, and expression s[k] is used for index
−n ≤ k < 0, what is the equivalent index j ≥ 0 such that s[j] references
the same element?
'''
import unittest


def func(seq, index):
    if index > 0:
        raise IndexError("The index must be negative")
    return seq[len(seq) + index]


class TestFunc(unittest.TestCase):
    def setUp(self):
        self.seq = [1, 2, 3, 4, 5]
        self.func = func

    def test_first_case(self):
        expected_result = self.seq[-1]
        func_result = self.func(self.seq, -1)
        self.assertEqual(expected_result, func_result)

    def test_second_case(self):
        expected_result = self.seq[-2]
        func_result = self.func(self.seq, -2)
        self.assertEqual(expected_result, func_result)


if __name__ == '__main__':
    unittest.main()

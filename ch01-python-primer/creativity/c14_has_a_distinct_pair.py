#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @first_date  20160807
# @date        20160807
'''C-1.14
Write a short Python function that takes a sequence of integer
values and determines if there is a distinct pair of numbers
in the sequence whose product is odd.
'''
import unittest


def has_a_distinct_pair(seq):
    length = len(seq)
    for i in xrange(length):
        for j in xrange(i + 1, length):
            # Check it's a distinct pair or not
            if set(seq[i]) != set(seq[j]):
                return 1
    return 0


class FuncTestCase(unittest.TestCase):
    def setUp(self):
        self.func = has_a_distinct_pair

    def test_first_case(self):
        seq = [[0, 0], [0, 1], [0, 2]]
        self.assertEqual(self.func(seq), 1)

    def test_second_case(self):
        seq = [[1, 2], [1, 2], [2, 1]]
        self.assertEqual(self.func(seq), 0)

    def test_third_case(self):
        seq = [[1, 2], [2, 1], [0, 0]]
        self.assertEqual(self.func(seq), 1)


if __name__ == '__main__':
    unittest.main()

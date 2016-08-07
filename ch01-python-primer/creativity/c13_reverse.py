#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @first_date  20160807
# @date        20160807
'''C-1.13
Write a pseudo-code description of a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than they
were before, and compare this method to an equivalent Python function
'''
import unittest


def reverse(seq):
    return seq[::-1]


def reverse_by_sort(seq):
    length = len(seq)
    for start_index in xrange(length // 2):
        end_index = length - start_index - 1
        seq[start_index], seq[end_index] = seq[end_index], seq[start_index]
    return seq


class ReverseTestCase(unittest.TestCase):
    def setUp(self):
        self.func = reverse

    def test_func(self):
        list_ = list(xrange(10))
        self.assertEqual(list_[::-1], self.func(list_))


class ReverseBySortTestCase(ReverseTestCase):
    def setUp(self):
        self.func = reverse_by_sort


if __name__ == '__main__':
    unittest.main()

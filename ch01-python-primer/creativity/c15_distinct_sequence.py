#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @first_date  20160811
# @date        20160811
'''C-1.15
Write a Python function that takes a sequence of numbers
and determines if all the numbers are different from each
other (that is, they are distinct).
'''
import unittest


def func1(seq):
    """Used built-in function to slove"""
    return list(set(seq))


def func2(seq):
    """Used dict to filter seq"""
    dict_ = {}

    for num in seq:
        if num in dict_:
            dict_[num] += 1
        else:
            dict_[num] = 0

    return dict_.keys()


def func3(seq):
    """This case is worse than func2"""
    def collect_elements(dict_, element):
        if element in dict_:
            dict_[element] += 1
        else:
            dict_[element] = 0
        return dict_

    collections = reduce(collect_elements, seq, {})
    return collections.keys()


class TestFunc1(unittest.TestCase):
    input_seq = [0, 1, 2, 1, 3, 2]
    expected_seq = [0, 1, 2, 3]

    def setUp(self):
        self.func = func1

    def test_func(self):
        set1 = set(self.func(self.input_seq))
        set2 = set(self.expected_seq)
        print set1, set2
        self.assertEqual(set1, set2)


class TestFunc2(TestFunc1):
    def setUp(self):
        self.func = func2


class TestFunc3(TestFunc1):
    def setUp(self):
        self.func = func3


if __name__ == '__main__':
    unittest.main()

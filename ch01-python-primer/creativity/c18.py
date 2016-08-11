#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @first_date  20160811
# @date        20160811
'''C-1.18
'''
import unittest


def func():
    seq = [0]
    for i in range(1, 10):
        seq.append(seq[-1] + 2 * i)
    return seq


def func2():
    seq = []
    last_num = 0
    for i in range(0, 10):
        seq.append(last_num + 2 * i)
        last_num = seq[i]
    return seq


class TestFunc(unittest.TestCase):
    expected_output = [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]

    def setUp(self):
        self.func = func

    def test_first_case(self):
        self.assertEqual(self.func(), self.expected_output)


class TestFunc2(unittest.TestCase):
    def setUp(self):
        self.func = func2


if __name__ == '__main__':
    unittest.main()

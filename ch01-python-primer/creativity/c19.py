#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @first_date  20160811
# @date        20160811
'''C-
'''
import unittest


def func():
    return [chr(97 + i) for i in range(26)]


def func2():
    import string
    return list(string.ascii_lowercase)


def func3():
    import string
    return [word for word in string.ascii_lowercase]


class TestFunc(unittest.TestCase):
    expected_output = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
        'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z'
    ]

    def setUp(self):
        self.func = func

    def test_correctness(self):
        self.assertEqual(self.func(), self.expected_output)


class TestFunc2(TestFunc):
    def setUp(self):
        self.func = func2


class TestFunc3(TestFunc):
    def setUp(self):
        self.func = func3


if __name__ == '__main__':
    unittest.main()

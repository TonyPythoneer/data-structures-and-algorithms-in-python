#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @first_date  20160801
# @date        20160801
'''R-1.9
What parameters should be sent to the range constructor,
to produce a range with values 50, 60, 70, 80?
'''
import unittest


def func():
    return list(xrange(50, 90, 10))


class TestFunc(unittest.TestCase):
    def setUp(self):
        self.func = func

    def test_first_case(self):
        expected_result = [50, 60, 70, 80]
        self.assertEqual(expected_result, self.func())

if __name__ == '__main__':
    unittest.main()

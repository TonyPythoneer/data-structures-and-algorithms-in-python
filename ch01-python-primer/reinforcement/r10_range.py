#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @first_date  20160804
# @date        20160804
'''R-1.10
What parameters should be sent to the range constructor,
to produce a range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?
'''
import unittest


def func():
    return list(xrange(8, -10, -2))


class Test(unittest.TestCase):
    def setUp(self):
        self.func = func

    def test_first_case(self):
        expect_result = [8, 6, 4, 2, 0, -2, -4, -6, -8]
        self.assertEqual(expect_result, self.func())


if __name__ == '__main__':
    unittest.main()

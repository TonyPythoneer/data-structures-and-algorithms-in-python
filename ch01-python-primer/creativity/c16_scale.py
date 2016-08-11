#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @first_date  20160811
# @date        20160811
'''C-
'''
import unittest


def func(data):
    pass


class Test(unittest.TestCase):
    def setUp(self):
        self.func = func


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @first_date  20160801
# @date        20160801
'''
'''
import unittest


def func(data):
    pass


class Test(unittest.TestCase):
    def setUp(self):
        self.func = func


if __name__ == '__main__':
    unittest.main()

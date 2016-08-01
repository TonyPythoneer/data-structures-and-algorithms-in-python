#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @first_date  20160801
# @date        20160801
'''R-1.7
Give a single command that computes the sum from Exercise R-1.6, relying on
Python’s comprehension syntax and the built-in sum function
'''
from sys import argv

from r6_sum_odds import func_with_sum as func


def input_num():
    # Verify the length
    if len(argv) < 2:
        raise IndexError('The command args are less than 2')

    # Fetch necessary arg and verify the arg
    try:
        num = int(argv[1])
    except ValueError as err:
        err.message = 'Required integer number'
        raise

    return num


if __name__ == '__main__':
    num = input_num()
    print func(num)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @first_date  20160731
# @date        20160731
'''R-1.5
Give a single command that computes the sum from Exercise
R-1.4, relying on Python’s comprehension syntax and the
built-in sum function.
'''
from sys import argv

from r4_trapezoidal import trapezoidal_algorithm as algorithm


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
    print algorithm(num)

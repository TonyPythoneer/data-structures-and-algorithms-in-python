#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @first_date  20160807
# @date        20160807
'''R-1.12
Python’s random module includes a function choice(data) that returns
a random element from a non-empty sequence. The random module
includes a more basic function randrange, with parameterization
similar to the built-in range function, that return a random choice
from the given range. Using only the randrange function, implement
your own version of the choice function.
'''
from random import randint


def randrange(start, end, step=None):
    if step and isinstance(step, int):
        rand_args = (start, end, step)
    else:
        rand_args = (start, end)
    seq = tuple(xrange(*rand_args))
    rand_index = randint(0, len(seq) - 1)
    return seq[rand_index]


if __name__ == '__main__':
    print randrange(0, 10)

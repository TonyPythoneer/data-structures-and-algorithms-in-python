#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @first_date  20160811
# @date        20160811
'''C-1.20
'''
import random


def shuffle(data):
    random_indexes = []
    length = len(data)
    maxint = length - 1
    while (length > 0):
        index = random.randint(0, maxint)
        if index not in random_indexes:
            random_indexes.append(index)
            length -= 1
    return map(lambda index: data[index], random_indexes)


if __name__ == '__main__':
    print shuffle(list(range(0, 10)))

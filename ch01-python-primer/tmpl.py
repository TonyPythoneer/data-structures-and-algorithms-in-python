#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @first_date  20160811
# @date        20160811
'''C-1.16
In our implementation of the scale function (page 25), the body of the loop
executes the command data[j] = factor. We have discussed that numeric types
are immutable, and that use of the = operator in this context causes the
creation of a new instance (not the mutation of an existing instance).
How is it still possible, then, that our implementation of scale changes
the actual parameter sent by the caller?
'''
import unittest


def scale(data, factor):
    for i in range(len(data)):
        data[i] *= factor


class TestFunc(unittest.TestCase):
    def setUp(self):
        self.func = func

    def test_the_seq_has_changed_by_func(self):
        """In fact, list is mutable

        Although func doesn't return to input_seq, it has changed input_seq.

        When the data parameter of scale sent by the caller, it does call
        by reference, not call by value, so it causes changed.
        """
        input_seq = [1, 2, 3]
        self.func(input_seq, 3)
        self.assertEqual(input_seq, map(lambda x: x * 3, [3, 6, 9]))

    def test_the_seq_has_not_changed_by_map(self):
        """Another example that uses map doesn't change data

        According to this operation, it proves thant it doesn't change
        """
        input_seq = [1, 2, 3]
        map_seq = map(lambda x: x * 3, input_seq)
        self.assertEqual(input_seq, map_seq)



if __name__ == '__main__':
    unittest.main()

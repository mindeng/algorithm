#! /usr/bin/env python

"""
A special stack implementation, with a method min() which can
return the current minimum value from the stack.
"""
class StackWithMin:

    def __init__(self):
        self._values = []
        self._mins = []

    def push(self, v):
        # push v
        self._values.append(v)
        
        # push into _mins if v is the current minimum value
        if len(self._mins) == 0 or v <= self._mins[-1]:
            self._mins.append(v)

    def pop(self):
        v = self._values.pop()

        # pop from _mins if v is the current minimum value
        if v == self._mins[-1]:
            self._mins.pop()

        return v

    def top(self):
        return self._values[-1]

    def size(self):
        return len(self._values)

    def is_empty(self):
        return len(self._values) == 0

    def empty(self):
        del self._values[:]
        del self._mins[:]

    def min(self):
        return self._mins[-1]

import unittest
import random

class TestStackWithMin(unittest.TestCase):

    def test_push(self):
        s = StackWithMin()
        map(s.push, xrange(100))
        self.assertEqual(s.size(), 100)
        self.assertEqual(s._values, range(100))

    def test_pop(self):
        s = StackWithMin()
        map(s.push, xrange(100))

        [self.assertEqual(s.pop(), i) for i in xrange(99, -1, -1)]
        self.assertEqual(s.size(), 0)

    def test_min(self):
        s = StackWithMin()
        L = range(100)
        random.shuffle(L)
        map(s.push, L)

        while len(L) > 0:
            self.assertEqual(s.min(), min(L))
            s.pop()
            L.pop()

if __name__ == '__main__':
    unittest.main()

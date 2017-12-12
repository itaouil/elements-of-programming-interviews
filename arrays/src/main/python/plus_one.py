"""
    Given an array that encodes a
    non-negative integer (D) produce an
    algorithm that returns the encoding
    of D + 1.

    Time    : O(n)
    Space   : O(1)
"""

import unittest

def plus_one(a):

    # Reminder
    rem = 1

    for x in reversed(range(len(a))):

        tmp_sum = a[x] + rem
        if tmp_sum < 10:
            a[x] = tmp_sum
            break

        else:
            a[x] = 0
            rem = 1

    return a

class TestPlusOne(unittest.TestCase):

    def test_plus_one(self):
        self.assertEqual([1, 9, 9, 5], plus_one([1, 9, 9, 4]))
        self.assertEqual([1, 3, 0], plus_one([1, 2, 9]))
        self.assertEqual([2, 0, 0, 0], plus_one([1, 9, 9, 9]))

if __name__ == '__main__':
    unittest.main()

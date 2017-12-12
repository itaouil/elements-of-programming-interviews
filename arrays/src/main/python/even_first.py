"""
    Re-order the array such as to have
    even numbers to come first in the
    array and odd numbers afterwards.

    Time    : O(n)
    Space   : O(1)
"""

import unittest

def even_first(a):

    # Left and right boundaries
    l, r = 0, len(a) - 1

    # Keep re-ordering
    while l < r:

        # Check if number is
        # odd and move it to
        # odd subarray
        if a[l] % 2 != 0:
            tmp = a[l]
            a[l] = a[r]
            a[r] = tmp
            r -= 1

            # Otherwise number is
            # even and move on to
            # next check
        else:
            l += 1

    return a

class TestStringMethods(unittest.TestCase):

    def test_even(self):
        self.assertEqual([10,6,4,9,7,3], even_first([3, 7, 4, 6, 9, 10]))
        self.assertEqual([2, 8, 6, 7, 9], even_first([2, 9, 6, 7, 8]))
        self.assertEqual([2, 9], even_first([9, 2]))
        self.assertEqual([2], even_first([2]))

if __name__ == '__main__':
    unittest.main()

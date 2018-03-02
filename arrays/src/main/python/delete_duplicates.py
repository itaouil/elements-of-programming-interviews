"""
    Delete duplicates from
    sorted array.

    Time    : O(n)
    Space   : O(1)
"""

import unittest

def remove_duplicates(A):

    if not A:
        return 0

    write = 1
    for i in range(1, len(A)):
        if A[write - 1] != A[i]:
            A[write] = A[i]
            write += 1

    return A[:write]

class TestRemoveDuplicate(unittest.TestCase):

    def test(self):
        self.assertEqual([2,3,5,7,11,13], remove_duplicates([2,3,5,5,7,11,11,11,13]))

if __name__ == '__main__':
    unittest.main()

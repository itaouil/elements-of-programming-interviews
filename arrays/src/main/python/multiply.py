"""
    Write a function that computes
    multiplication on arrays encoding
    integers

    Time    : O(nm)
    Space   : O(1)
"""

import unittest

def multiply(num1, num2):

    # Get sign of the multiplication
    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])

    # Resulting array (we have at most n + m digits in the result)
    res = [0] * (len(num1) + len(num2))

    # Multiplication
    for j in reversed(range(len(num1))):
        for i in reversed(range(len(num2))):
            res[i + j + 1] += num1[j] * num2[i]
            res[i + j] += res[i + j + 1] // 10
            res[i + j + 1] %= 10

    # Get rid of leading zeroes
    res = res[next((i for i, x in enumerate(res) if x != 0), len(res)):] or [0]

    # Return result
    return [sign * res[0]] + res[1:]

class TestPlusOne(unittest.TestCase):

    def test_plus_one(self):
        self.assertEqual([6,6,4,2], multiply([1,2,3], [5,4]))
        self.assertEqual([-1,9,9,0,9,2,0], multiply([8,4,7,2], [-2,3,5]))

if __name__ == '__main__':
    unittest.main()

"""
    Advance through an array.

    Time    : O(n)
    Space   : O(1)
"""

import unittest

def can_reach_end(a):

    furthest_reach_so_far, last_index = 0, len(a) - 1
    i = 0

    while i <= furthest_reach_so_far and furthest_reach_so_far < last_index:
        furthest_reach_so_far = max(furthest_reach_so_far, a[i] + i)
        i += 1

    return furthest_reach_so_far >= last_index

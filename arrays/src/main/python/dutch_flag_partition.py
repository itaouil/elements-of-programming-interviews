"""
    Re-order the array such that
    all elements less than the pivot
    comes first, followed by elements
    equal to the pivot followed by
    elements greater than the pivot.

    Time    : O(n)
    Space   : O(1)
"""

import unittest

def dutch_flag_partition(a, pivot_index):

    # Indices & pivot
    pivot = a[pivot_index]
    smaller, equal, larger = 0, 0, len(a) - 1

    # Iterate until array sorted
    while equal < larger:

        if a[equal] < pivot:
            a[smaller], a[equal] = a[equal], a[smaller]
            smaller, equal = smaller + 1, equal + 1

        elif a[equal] == pivot:
            equal += 1

        else:
            a[larger], a[equal] = a[equal], a[larger]
            larger -= 1

    return a

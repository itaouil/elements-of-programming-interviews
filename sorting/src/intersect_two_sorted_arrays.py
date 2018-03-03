"""
    Given two sorted arrays
    find their intersection
    maintaining the sorting.
"""

import bisect

# Not optimal way of doing it:
# Iterate over one arrays and
# check if it does exist in the
# other array
# def intersect_two_sorted_arrays(A, B):
#     return [a for i, a in enumerate(A) if(i == 0 or a != A[i-1]) and a in B]

# Not so optimal way of doing it:
# Iterate over one arrays and
# check if it does exist in the
# other array (using binary search)
# def intersect_two_sorted_arrays(A, B):
#
#     # Check if element is present in B (bin. search)
#     def is_present(k):
#         i = bisect.bisect_left(B, k)
#         return i < len(B) and B[i] == k
#
#     return [a for i, a in enumerate(A) if(i == 0 or a != A[i-1]) and is_present(a)]

# Optimal way of solving the problem:
# By increasing the iterators at the
# same time
def intersect_two_sorted_arrays(A, B):

    i, j, inter = 0, 0, []

    while i < len(A) and j < len(B):

        if A[i] == B[j] and A[i] != A[i - 1]:
            inter.append(A[i])
            i += 1
            j += 1

        elif A[i] < B[j]:
            i += 1

        else:
            j += 1

    return inter

print(intersect_two_sorted_arrays([2,3,3,5,5,6,7,7,8,12], [5,5,6,8,8,9,10,10]))

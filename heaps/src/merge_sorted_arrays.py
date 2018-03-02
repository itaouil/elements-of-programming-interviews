"""
    Merge sorted arrays using
    heaps and the python implementation
    of it.

    Running time:
        O(n * logk), where n is the # of elements and k the # of sequences
"""

# Import heap implementation
import heapq

def merge_sorted_arrays(sorted_arrays):

    # Creat empty list
    # which is going to
    # be used for the push
    # and pop actions.
    min_heap = []

    # Get iterators for each array
    sorted_arrays_iter = [iter(x) for x in sorted_arrays]

    # Get first three elements from
    # the sorted arrays
    for i, it in enumerate(sorted_arrays_iter):
        first_element = next(it, None)
        if first_element is not None:
            heapq.heappush(min_heap, (first_element, i))

    # Pop from heap smalles element
    # and at the same time push onto
    # the heap the next smallest element
    result = []
    while min_heap:
        # Get smallest entry in the heap
        # and the array it is from
        smallest_element, smallest_array_entry = heapq.heappop(min_heap)

        # Get smallest array entry iterator
        smallest_array_iter = sorted_arrays_iter[smallest_array_entry]

        # Push smallest element in the heap
        result.append(smallest_element)

        # Push next element.
        # Which is coming from the array
        # that had the smallest element
        next_element = next(smallest_array_iter, None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, smallest_array_entry))

    return result

print(merge_sorted_arrays([[3,5,6], [0,6], [0,6,28]]))

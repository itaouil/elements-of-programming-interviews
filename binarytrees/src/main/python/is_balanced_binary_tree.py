"""
    Function that checks whether
    a binary tree is height balanced.

    Time    : O(n)
    Space   : O(1)
"""

import collections

def is_balanced_binary_tree(tree):

    # Create a tuple collection
    status = collections.namedtuple('status', ('balanced', 'height'))

    # Call check balanace function
    check_balance(tree)

    # Recursive balanced function
    def check_balance(tree):

        # Base case
        if not tree:
            return status(True, -1)

        # Recursive left subtree call
        left = check_balance(tree.left)
        if not left.balanced:
            # Left subtree not balanced
            return status(False, 0)

        # Recursive right subtree call
        right = check_balance(tree.right)
        if not right.balanced:
            # Right subtree not balanced
            return status(False, 0)

        # Both subtrees balanced
        is_balanced = abs(left.height - right.height) < 2
        height = max(left.height, right.height) + 1
        return status(is_balanced, height)

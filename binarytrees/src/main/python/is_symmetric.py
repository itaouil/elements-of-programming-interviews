"""
    Function that checks whether
    a binary tree is symmetric.

    Time    : O(n)
    Space   : O(h)
"""

def check_symmetry(tree):

    def is_symmetric(subtree0, subtree1):

        if not subtree0 and not subtree1:
            return True

        elif subtree0 and subtree1:
            return (subtree0.data == subtree1.data and is_symmetric(subtree0.left, subtree1.right) and is_symmetric(subtree0.right, subtree1.left))

        else:
            return False

    return not tree or is_symmetric(tree.left, tree.right)

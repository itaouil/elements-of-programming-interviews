"""
    Find the lowest common
    ancestor when the nodes
    do not have the reference
    to their parent.

    Time    : O(n)
    Space   : O(1)
"""

def lca(root, node1, node2):

    # Check if root is LCA
    if root in [node1, node2]:
        return root

    # Recursive calls to left and right subtrees
    left = lca(root.left, node1, node2)
    right = lca(root.right, node1, node2)

    # Return values up in the stack
    if left == None and right == None:
        return None

    elif left != None and right != None:
        return root

    else:
        return left if left != None else right

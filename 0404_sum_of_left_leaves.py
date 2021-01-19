# Find the sum of all left leaves in a given binary tree.

# Example:

#     3
#    / \
#   9  20
#     /  \
#    15   7

# There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.


from utils import *


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def traverse(root, is_left):
            if root is None:
                return 0
            if root.left is None and root.right is None and is_left:  # this is a left leaf
                return root.val
            s_left = traverse(root.left, True)
            s_right = traverse(root.right, False)
            return s_left + s_right
        return traverse(root, False)

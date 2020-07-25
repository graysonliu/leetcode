# Given a binary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given binary tree [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its depth = 3.

from utils import *


class Solution:
    max_depth = 0

    def maxDepth(self, root: TreeNode) -> int:
        def traverse(root, level):
            if root is None:
                return
            self.max_depth = max(self.max_depth, level)
            traverse(root.left, level + 1)
            traverse(root.right, level + 1)

        traverse(root, 1)
        return self.max_depth

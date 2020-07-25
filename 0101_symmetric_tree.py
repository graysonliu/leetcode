# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#
# But the following [1,2,2,null,3,null,3] is not:
#
#     1
#    / \
#   2   2
#    \   \
#    3    3
#
# Follow up: Solve it both recursively and iteratively.

from utils import *


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def flip_equal(r1, r2):
            if r1 is None and r2 is None:
                return True
            if r1 and r2 and r1.val == r2.val:
                return flip_equal(r1.left, r2.right) and flip_equal(r1.right, r2.left)
            return False

        return True if root is None else flip_equal(root.left, root.right)

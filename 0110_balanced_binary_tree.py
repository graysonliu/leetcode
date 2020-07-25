# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as:
#
# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
#
# Example 1:
#
# Given the following tree [3,9,20,null,null,15,7]:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Return true.
#
# Example 2:
#
# Given the following tree [1,2,2,3,3,null,null,4,4]:
#
#        1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
# Return false.

from utils import *


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def depth(root):
            if root is None:
                return 0
            depth_l = depth(root.left)
            if depth_l == -1:
                return -1  # left subtree is unbalanced
            depth_r = depth(root.right)
            if depth_r == -1:
                return -1  # right subtree is unbalanced
            if max(depth_l, depth_r) - min(depth_l, depth_r) > 1:
                return -1  # this tree is unbalanced
            return max(depth_l, depth_r) + 1  # return depth of this tree

        return depth(root) != -1

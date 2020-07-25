# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given the below binary tree and sum = 22,
#
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \    / \
# 7    2  5   1
# Return:
#
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]

from utils import *
from typing import List


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []

        def backtrack(root, path, s):
            if root is None:
                return
            s += root.val
            if root.left is None and root.right is None and s == sum:
                res.append(path + [root.val])
                return
            backtrack(root.left, path + [root.val], s)
            backtrack(root.right, path + [root.val], s)

        backtrack(root, [], 0)
        return res

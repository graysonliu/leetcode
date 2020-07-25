# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]

from utils import *
from typing import List


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []

        def traverse(root, level):
            if root is None:
                return
            while len(res) <= level:
                res.append([])
            res[level].append(root.val)
            traverse(root.left, level + 1)
            traverse(root.right, level + 1)

        traverse(root, 0)
        return res

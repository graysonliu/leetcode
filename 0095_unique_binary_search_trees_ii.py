# Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.
#
# Example:
#
# Input: 3
# Output:
# [
#   [1,null,3,2],
#   [3,2,null,1],
#   [3,1,null,null,2],
#   [2,1,3],
#   [1,null,2,null,3]
# ]
# Explanation:
# The above output corresponds to the 5 unique BST's shown below:
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

# Constraints:
#
# 0 <= n <= 8

from utils import *
from typing import List


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        cache = {}

        def gen_tree(start, end):
            trees = []
            if (start, end) in cache:
                return cache[(start, end)]
            elif start > end:
                return [None]
            else:
                for i in range(start, end + 1):
                    for left in gen_tree(start, i - 1):
                        for right in gen_tree(i + 1, end):
                            node = TreeNode(i)
                            node.left = left
                            node.right = right
                            trees.append(node)
                cache[(start, end)] = trees
                return trees

        return gen_tree(1, n) if n != 0 else []

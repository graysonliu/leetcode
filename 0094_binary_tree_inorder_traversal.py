# Given a binary tree, return the inorder traversal of its nodes' values.
#
# Example:
#
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# Output: [1,3,2]
# Follow up: Recursive solution is trivial, could you do it iteratively?

from utils import *
from typing import List


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def traverse_recursive(root):
            if root is None:
                return
            traverse_recursive(root.left)
            res.append(root.val)
            traverse_recursive(root.right)

        def traverse_iterative(root):
            stack = []

            def traverse_left(node):
                while node:
                    stack.append(node)
                    node = node.left

            traverse_left(root)
            while len(stack) > 0:
                node = stack.pop()
                res.append(node.val)
                traverse_left(node.right)

        # traverse_recursive(root)
        traverse_iterative(root)
        return res

# Given a binary tree, return the preorder traversal of its nodes' values.
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
# Output: [1,2,3]
# Follow up: Recursive solution is trivial, could you do it iteratively?

from utils import TreeNode
from typing import List


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        # recursive version
        def traverse_recursive(node):
            if node is None:
                return
            res.append(node.val)
            traverse_recursive(node.left)
            traverse_recursive(node.right)

        # iterative version
        # basically an iterative version of DFS
        # first in last out
        def traverse_iterative(root):
            stack = [root]
            while len(stack) > 0:
                node = stack.pop()
                if node is not None:
                    res.append(node.val)
                    stack.append(node.right)
                    stack.append(node.left)

        # traverse_recursive(root)
        traverse_iterative(root)
        return res

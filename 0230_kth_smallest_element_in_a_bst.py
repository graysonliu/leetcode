# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
#
#
#
# Example 1:
#
# Input: root = [3,1,4,null,2], k = 1
#       3
#      / \
#     1   4
#      \
#       2
# Output: 1
# Example 2:
#
# Input: root = [5,3,6,2,4,null,null,1], k = 3
#       5
#      / \
#     3   6
#    / \
#   2   4
#  /
# 1
# Output: 3
# Follow up:
# What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
#
#
#
# Constraints:
#
# The number of elements of the BST is between 1 to 10^4.
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

from utils import *


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # recursive solution
        # self.k = k
        #
        # def inorder_traverse(root):
        #     if root is None:
        #         return
        #
        #     l_res = inorder_traverse(root.left)
        #     if l_res:
        #         return l_res
        #
        #     # inorder traverse visits values from smallest to largest
        #     self.k -= 1
        #     if self.k == 0:
        #         return root
        #
        #     r_res = inorder_traverse(root.right)
        #     if r_res:
        #         return r_res
        #
        # return inorder_traverse(root).val

        # iterative solution: iterations are easier to control
        # iterative inorder traverse: #0094
        stack = []

        def traverse_left(node):
            while node is not None:
                stack.append(node)
                node = node.left

        traverse_left(root)
        while len(stack) > 0:
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            traverse_left(node.right)

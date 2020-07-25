# Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
#
# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
#
# Example:
#
# Given the sorted linked list: [-10,-3,0,5,9],
#
# One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
#
#       0
#      / \
#    -3   9
#    /   /
#  -10  5

from utils import *


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        nums = []
        p = head
        while p:
            nums.append(p.val)
            p = p.next

        def toTree(nums):
            if len(nums) == 0:
                return None
            i = (len(nums) - 1) // 2
            root = TreeNode(nums[i])
            root.left = toTree(nums[:i])
            root.right = toTree(nums[i + 1:])
            return root

        return toTree(nums)

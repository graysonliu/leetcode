# Given preorder and inorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.
#
# For example, given
#
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
# Return the following binary tree:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7

from utils import *
from typing import List


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        else:
            root = TreeNode(preorder[0])
            i = inorder.index(preorder[0])
            root.left = self.buildTree(preorder[1:1 + i], inorder[:i])
            root.right = self.buildTree(preorder[1 + i:], inorder[i + 1:])
            return root

# Given a binary tree, flatten it to a linked list in-place.
#
# For example, given the following tree:
#
#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
# The flattened tree should look like:
#
# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6

from utils import *


class Solution:
    last_visited_node_in_the_left_subtree = None

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # using pre-order traverse
        # we need to find the last visited node in the left subtree
        # since this node will be the parent of the root of the right subtree
        if root is None:
            return
        self.last_visited_node_in_the_left_subtree = root
        self.flatten(root.left)
        if self.last_visited_node_in_the_left_subtree == root:  # this means left subtree is None
            self.flatten(root.right)
        else:
            self.last_visited_node_in_the_left_subtree.right = root.right
            root.right = root.left
            root.left = None
            self.flatten(self.last_visited_node_in_the_left_subtree.right)

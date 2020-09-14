# The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.
#
# Determine the maximum amount of money the thief can rob tonight without alerting the police.
#
# Example 1:
#
# Input: [3,2,3,null,3,null,1]
#
#       3
#      / \
#     2   3
#      \   \
#       3   1
#
# Output: 7
# Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
# Example 2:
#
# Input: [3,4,5,1,3,null,1]
#
#       3
#      / \
#     4   5
#    / \   \
#   1   3   1
#
# Output: 9
# Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.

from utils import *


class Solution:
    def rob(self, root: TreeNode) -> int:
        # for a tree node, we look into its left subtree and right subtree
        # if a node is robbed, then both its left child and right child cannot be robbed
        # its most recent descendants that we can rob are:
        # node.left.left, node.left.right, node.right.left, node.right.right

        dp = {}  # save maximum amount for each node if we start robbing from it (take it as the root)

        def rob_subtree(node):
            if node is None:
                return 0
            if node in dp:
                return dp[node]
            amount = 0
            if node.left:
                amount += rob_subtree(node.left.left) + rob_subtree(node.left.right)
            if node.right:
                amount += rob_subtree(node.right.left) + rob_subtree(node.right.right)
            res = max(node.val + amount, rob_subtree(node.left) + rob_subtree(node.right))
            dp[node] = res
            return res

        return rob_subtree(root)

        # another solution: we record amounts along the way of recursions
        # taking each node as the root, we need to record two values
        # one is the maximum amount if this node is robbed
        # another is the maximum amount if this node is not robbed
        def rob_subtree_new(node):
            if node is None:
                return 0, 0  # robbed, not robbed as stated before
            left = rob_subtree_new(node.left)
            right = rob_subtree_new(node.right)
            return node.val + left[1] + right[1], max(left) + max(right)

        return max(rob_subtree_new(root))


print(Solution().rob(list_to_tree([4, 1, None, 2, None, 3])))

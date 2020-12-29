# Given a non-empty binary tree, find the maximum path sum.
#
# For this problem, a path is defined as any node sequence from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.
#
#
# Example 1:
#
# Input: root = [1,2,3]
# Output: 6
# Example 2:
#
#
# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 3 * 104].
# -1000 <= Node.val <= 1000

from utils import *


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res = float('-inf')

        # for each node, we calculate its max path sum of one side first (left side or right side)
        def max_path_one_side(node):
            if node is None:
                return 0
            # postorder traverse
            left_max = max(max_path_one_side(node.left), 0)
            right_max = max(max_path_one_side(node.right), 0)
            # if this node is the pivot of the entire path, we get its max possible path sum
            nonlocal res
            res = max(res, node.val + left_max + right_max)
            return max(left_max, right_max) + node.val

        max_path_one_side(root)
        return res

# You are given the root of a binary search tree (BST), where exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.
#
# Follow up: A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
#
# Example 1:
#
# Input: root = [1,3,null,null,2]
# Output: [3,1,null,null,2]
# Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.
# Example 2:
#
# Input: root = [3,1,4,null,null,2]
# Output: [2,1,4,null,null,3]
# Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.
#
# Constraints:
#
# The number of nodes in the tree is in the range [2, 1000].
# -231 <= Node.val <= 231 - 1

from utils import *


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        # for a BST, we use inorder traverse to flatten it, the flattened form is ascending
        # if nodes numbers are swapped in the BST, in the flattened form, there will be two descending abnormal points
        # suppose they are [..., a1, a2,..., a3, a4,...], a1>a2, a3>a4, the two swapped nodes are a1 and a4
        # special case: only one descending abnormal points if those two swapped nodes are adjacent

        # use pre to record the last traversed node
        pre = None
        # the first node of the swapped pair
        swap1, swap2 = None, None

        def traverse(node):
            if node is None:
                return

            # inorder
            traverse(node.left)

            nonlocal pre, swap1, swap2
            if (pre and pre.val > node.val):  # found one of those swapped nodes
                if not swap1:
                    swap1 = pre
                # the following line will handle both cases whether swapped nodes are adjacent or not
                swap2 = node

            pre = node
            traverse(node.right)

        traverse(root)
        swap1.val, swap2.val = swap2.val, swap1.val


Solution().recoverTree(list_to_tree([1, 3, None, None, 2]))

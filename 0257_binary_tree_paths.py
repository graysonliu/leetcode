# Given a binary tree, return all root-to-leaf paths.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Input:
#
#   1
#  / \
# 2   3
#  \
#   5
#
# Output: ["1->2->5", "1->3"]
#
# Explanation: All root-to-leaf paths are: 1->2->5, 1->3

from typing import List

from utils import TreeNode


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []

        # backtrack
        def backtrack(root, path):
            if not root:
                return
            if not root.left and not root.right:
                path.append(str(root.val))
                res.append('->'.join(path))
                path.pop()
                return
            path.append(str(root.val))
            backtrack(root.left, path)
            backtrack(root.right, path)
            path.pop()

        backtrack(root, [])
        return res

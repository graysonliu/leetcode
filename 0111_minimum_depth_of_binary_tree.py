# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given binary tree [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its minimum depth = 2.


from utils import *


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # bfs
        if root is None:
            return 0
        import queue
        Q = queue.Queue()
        Q.put((root, 1))
        while not Q.empty():
            root, depth = Q.get()
            if root.left is None and root.right is None:
                return depth
            if root.left:
                Q.put((root.left, depth + 1))
            if root.right:
                Q.put((root.right, depth + 1))

# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
#
# Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]
#
# Example 1:
#
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
# Example 2:
#
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
#
#
# Note:
#
# All of the nodes' values will be unique.
# p and q are different and both values will exist in the binary tree.

from utils import *


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # my recursive solution: find path to p and q respectively
        # then compare those two paths, the last common node is the lowest common ancestor
        self.path_p = list()
        self.path_q = list()

        def backtrack(root, path, p, q):
            if root is None:
                return
            if len(self.path_p) > 0 and len(self.path_q) > 0:  # we have found paths to p and q, no more recursion
                return
            if root == p:
                self.path_p = path + [root]
            elif root == q:
                self.path_q = path + [root]
            # using append() and pop() for path before and after recursion invocation
            # rather than using path+[root] in recursion invocation directly
            # this will significantly improve the performance
            path.append(root)
            backtrack(root.left, path, p, q)
            backtrack(root.right, path, p, q)
            path.pop()

        # find the last common node in two paths
        backtrack(root, [], p, q)
        res = None
        for i in range(min(len(self.path_p), len(self.path_q))):
            if self.path_p[i] == self.path_q[i]:
                res = self.path_p[i]
        return res

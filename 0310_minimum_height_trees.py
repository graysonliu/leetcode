# A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.
#
# Given a tree of n nodes and n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).
#
# Return a list of the root labels of all the MHTs. You can return the answer in any order.
#
# The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.
#
#
#
# Example 1:
#
#
# Input: n = 4, edges = [[1,0],[1,2],[1,3]]
# Output: [1]
# Explanation: As shown, the height of the tree is 1 when the root is one which is the only MHT.
# Example 2:
#
#
# Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
# Output: [3,4]
# Example 3:
#
# Input: n = 1, edges = []
# Output: [0]
# Example 4:
#
# Input: n = 2, edges = [[0,1]]
# Output: [0,1]
#
#
# Constraints:
#
# 1 <= n <= 2 * 10^4
# edges.length == n - 1
# 0 <= ai, bi < n
# ai != bi
# All the pairs (ai, bi) are distinct.
# The given input is guaranteed to be a tree.

from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # build adjacent list
        adj = {i: set() for i in range(n)}
        for edge in edges:
            adj[edge[0]].add(edge[1])
            adj[edge[1]].add(edge[0])
        # solution: https://leetcode.com/problems/minimum-height-trees/discuss/76055/Share-some-thoughts
        # note: a tree with n vertices has exactly n-1 edges
        # the degree of leaf node is 1
        # this approach is like a reversed BFS
        # we first find all leaf nodes, and remove all these leaf nodes from the graph
        # then, we will have some new leaf nodes
        # repeat previous procedure util we have only 1 or 2 vertices
        leaves = [v for v in adj.keys() if len(adj[v]) == 1]
        while len(adj) > 2:
            for leaf in leaves:
                adj[adj[leaf].pop()].remove(leaf)
                adj.pop(leaf)
            leaves = [v for v in adj.keys() if len(adj[v]) == 1]
        return list(adj.keys())


print(Solution().findMinHeightTrees(n=6, edges=[[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]))

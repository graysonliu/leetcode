# You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.
#
# You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.
#
# Return the answers to all queries. If a single answer cannot be determined, return -1.0.
#
# Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.
#
#
#
# Example 1:
#
# Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
# Explanation:
# Given: a / b = 2.0, b / c = 3.0
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
# return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
# Example 2:
#
# Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
# Output: [3.75000,0.40000,5.00000,0.20000]
# Example 3:
#
# Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
# Output: [0.50000,2.00000,-1.00000,-1.00000]
#
#
# Constraints:
#
# 1 <= equations.length <= 20
# equations[i].length == 2
# 1 <= Ai.length, Bi.length <= 5
# values.length == equations.length
# 0.0 < values[i] <= 20.0
# 1 <= queries.length <= 20
# queries[i].length == 2
# 1 <= Cj.length, Dj.length <= 5
# Ai, Bi, Cj, Dj consist of lower case English letters and digits.

from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # construct a directed graph
        # for [a, b] in equations with value w, it represents two edges
        # edge a-->b whose weight is w, and edge b-->a whose weight is 1/w
        # for [c, d] in queries, this is to find a path between c and d, the evaluation should be the product of weights
        # of edges in this path

        # construct the graph
        from collections import defaultdict
        G = defaultdict(dict)
        for i, (start, end) in enumerate(equations):
            G[start][end] = values[i]
            G[end][start] = 1 / values[i]

        # find the path using DFS
        def dfs(start, end, visited):
            if end in G[start]:
                return G[start][end]
            for node in G[start]:
                if node not in visited:
                    visited.add(node)
                    prod = G[start][node] * dfs(node, end, visited)  # the product of weights
                    visited.remove(node)
                    if prod > 0:  # we found a path
                        return prod
            return 0  # we cannot find a path between start and end

        res = []

        for (start, end) in queries:
            if not (start in G and end in G):
                res.append(-1.0)
                continue
            prod = dfs(start, end, {start})
            res.append(-1.0 if prod == 0 else prod)

        return res


print(Solution().calcEquation(equations=[["a", "b"], ["b", "c"]], values=[2.0, 3.0],
                              queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]))

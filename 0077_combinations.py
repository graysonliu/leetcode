# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
#
# Example:
#
# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        # bfs
        import queue
        Q = queue.Queue()
        for i in range(1, n - k + 2):
            Q.put([i])
        while not Q.empty():
            node = Q.get()
            if len(node) == k:
                res.append(node)
            elif k - len(node) > n - node[-1]:  # not enough number left
                continue
            else:
                for i in range(node[-1] + 1, n + 1):
                    Q.put(node + [i])
        return res


print(Solution().combine(n=4, k=2))

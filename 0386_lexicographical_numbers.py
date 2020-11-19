# Given an integer n, return 1 - n in lexicographical order.
#
# For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].
#
# Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.

from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []

        # dfs
        def dfs(k):
            if k > n:
                return
            res.append(k)
            for j in range(0, 10):
                dfs(k * 10 + j)

        for i in range(1, 10):
            dfs(i)
        return res


print(Solution().lexicalOrder(13))

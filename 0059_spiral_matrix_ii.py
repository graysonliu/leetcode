# Given a positive integer n, generate a square matrix filled with elements from 1 to n^2 in spiral order.
#
# Example:
#
# Input: 3
# Output:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]

from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        layer = (n + 1) // 2
        m = []
        for i in range(n):
            m.append([0] * n)
        count = 1
        for l in range(layer):
            for i in range(l, n - l):
                m[l][i] = count
                count += 1
            for i in range(l + 1, n - l):
                m[i][n - 1 - l] = count
                count += 1
            for i in range(n - 2 - l, l - 1, -1):
                m[n - 1 - l][i] = count
                count += 1
            for i in range(n - 2 - l, l, -1):
                m[i][l] = count
                count += 1

        return m


print(Solution().generateMatrix(3))

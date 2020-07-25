# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
#
# Example 1:
#
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:
#
# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        try:
            width = len(matrix[0])
        except IndexError:
            width = 0
        height = len(matrix)
        layer = (min(width, height) + 1) // 2
        for l in range(layer):
            for i in range(l, width - l):
                result.append(matrix[l][i])
            for i in range(l + 1, height - l):
                result.append(matrix[i][width - 1 - l])
            if l != height - 1 - l:
                for i in range(width - 2 - l, l - 1, -1):
                    result.append(matrix[height - 1 - l][i])
            if l != width - 1 - l:
                for i in range(height - 2 - l, l, -1):
                    result.append(matrix[i][l])
        return result


print(Solution().spiralOrder([[6, 9, 7]]))

# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
#
# Example
# 1:
#
# Input:
# [
#     [1, 1, 1],
#     [1, 0, 1],
#     [1, 1, 1]
# ]
# Output:
# [
#     [1, 0, 1],
#     [0, 0, 0],
#     [1, 0, 1]
# ]
# Example
# 2:
#
# Input:
# [
#     [0, 1, 2, 0],
#     [3, 4, 5, 2],
#     [1, 3, 1, 5]
# ]
# Output:
# [
#     [0, 0, 0, 0],
#     [0, 4, 5, 0],
#     [0, 3, 1, 0]
# ]
#
# Follow up:
#
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvemencombt uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        columns = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    columns.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rows or j in columns:
                    matrix[i][j] = 0
        # print(matrix)


Solution().setZeroes([[0, 1, 2, 0],
                      [3, 4, 5, 2],
                      [1, 3, 1, 5]
                      ])

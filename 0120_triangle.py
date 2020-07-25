# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
#
# For example, given the following triangle
#
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
#
# Note:
#
# Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # backtracking (dfs) exceeds time limit
        # dynamic programming
        # from the bottom to the top, we calculate the minimum path sum from each node to the bottom row

        # for each node in the bottom row, the minimum path sum from it to the bottom row is just its own value
        # therefore, we initialize min_sum as the bottom row
        min_sum = triangle[-1]
        # we keep updating min_sum as we iterate rows from the bottom to the top
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                min_sum[j] = triangle[i][j] + min(min_sum[j], min_sum[j + 1])
        return min_sum[0]


print(Solution().minimumTotal([[2],
                               [3, 4],
                               [6, 5, 7],
                               [4, 1, 8, 3]]))

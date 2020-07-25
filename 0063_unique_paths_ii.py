# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#
# Now consider if some obstacles are added to the grids. How many unique paths would there be?

# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
#
# Note: m and n will be at most 100.
#
# Example 1:
#
# Input:
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# Output: 2
# Explanation:
# There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right

from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # dynamic programming
        # we denote the number of ways from start to obstacleGrid[i][j] as n[i][j]
        # since we can only go right or go down
        # if obstacleGrid[i][j] is not an obstacle, n[i][j] = n[i][j-1] + n[i-1][j] (left cell + upper cell)
        # if obstacleGrid[i][j] is an obstacle, n[i][j] = 0

        m = len(obstacleGrid)
        try:
            n = len(obstacleGrid[0])
        except IndexError:
            return 0

        # if the start point is an obstacle
        if obstacleGrid[0][0] == 1:
            return 0

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    obstacleGrid[0][0] = 1
                # not an obstacle
                elif obstacleGrid[i][j] == 0:
                    # first row
                    if i == 0:
                        obstacleGrid[i][j] = obstacleGrid[i][j - 1]
                    # first column
                    elif j == 0:
                        obstacleGrid[i][j] = obstacleGrid[i - 1][j]
                    else:
                        obstacleGrid[i][j] = obstacleGrid[i][j - 1] + obstacleGrid[i - 1][j]
                # meet an obstacle
                else:
                    obstacleGrid[i][j] = 0

        return obstacleGrid[-1][-1]


print(Solution().uniquePathsWithObstacles([[0, 0, 0],
                                           [0, 1, 0],
                                           [0, 0, 0]]))

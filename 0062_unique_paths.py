# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#
# How many possible unique paths are there?

# Example 1:
#
# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right
# Example 2:
#
# Input: m = 7, n = 3
# Output: 28

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        import math
        k = n - 1
        n = m + n - 2
        return int(math.factorial(n) / (math.factorial(n - k) * math.factorial(k)))


print(Solution().uniquePaths(7, 3))

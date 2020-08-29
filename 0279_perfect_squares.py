# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
#
# Example 1:
#
# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
# Example 2:
#
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.

class Solution:
    def numSquares(self, n: int) -> int:
        # dynamic programming
        dp = {0: 0}
        # dp[i] = min(dp[i-j*j]+1) for all j*j<=i
        for i in range(1, n + 1):
            dp[i] = float('inf')
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[n]


print(Solution().numSquares(12))

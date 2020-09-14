# Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.
#
# Example 1:
#
# Input: 2
# Output: 1
# Explanation: 2 = 1 + 1, 1 × 1 = 1.
# Example 2:
#
# Input: 10
# Output: 36
# Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
# Note: You may assume that n is not less than 2 and not larger than 58.

class Solution:
    def integerBreak(self, n: int) -> int:
        # dynamic programming solution
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], dp[j] * (i - j), j * (i - j))
        return dp[n]

        # mathematical solution
        # for any f, 1*(f-1)<f, therefore, there should not exist any 1 as a factor
        # for any f>=4, 2*(f-2)>=f, therefore, all factors should be less than than 4
        # thus, the only factors should be 2 and 3
        # since 6=2+2+2=3+3, but 2*2*2=8<3*3=9, so, every three '2' should be replaced by two '3'
        # that is, for any n>=6, we prefer '3' over '2'
        # for n=5, it is also divided into one '3' and one '2'
        # so, for any n>=5, we prefer '3' over '2'
        if n == 2:
            return 1
        if n == 3:
            return 2
        res = 1
        while n >= 5:
            n -= 3
            res *= 3
        # right now, n can only be 4 or 3 or 2
        res = res * n
        return res


print(Solution().integerBreak(10))

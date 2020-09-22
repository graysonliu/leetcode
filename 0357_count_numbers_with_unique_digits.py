# Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10^n.
#
# Example:
#
# Input: 2
# Output: 91
# Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100,
# excluding 11,22,33,44,55,66,77,88,99
#
#
# Constraints:
#
# 0 <= n <= 8

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        # n=0: 1
        # n=1: 1+9
        # n=2: 1+9+9*9, the first digit can choose from 1~9 since 0 should not be the head
        # the second digit have 9 options of 0~9 that excludes the one chosen as the first digit
        res = 1  # for n=0
        for i in range(1, n + 1):
            k = 9
            for j in range(1, i):
                k *= (10 - j)
            res += k
        return res


print(Solution().countNumbersWithUniqueDigits(2))

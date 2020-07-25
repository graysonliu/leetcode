# Implement pow(x, n), which calculates x raised to the power n (x^n).
#
# Example 1:
#
# Input: 2.00000, 10
# Output: 1024.00000
# Example 2:
#
# Input: 2.10000, 3
# Output: 9.26100
# Example 3:
#
# Input: 2.00000, -2
# Output: 0.25000
# Explanation: 2^(-2) = 1/2^2 = 1/4 = 0.25
# Note:
#
# -100.0 < x < 100.0
# n is a 32-bit signed integer, within the range [−2^31, 2^31 − 1]

class Solution:
    # binary exponential
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n == 0:
            return 1
        elif n == 1:
            return x
        else:
            div, mod = divmod(n, 2)
            p = self.myPow(x, div)
            return p * p * (x if mod == 1 else 1)


print(Solution().myPow(2.00000, -2147483648))

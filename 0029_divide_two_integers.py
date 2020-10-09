# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
#
# Return the quotient after dividing dividend by divisor.
#
# The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.
#
# Note:
#
# Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For this problem, assume that your function returns 2^31 − 1 when the division result overflows.
#
#
# Example 1:
#
# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10/3 = truncate(3.33333..) = 3.
# Example 2:
#
# Input: dividend = 7, divisor = -3
# Output: -2
# Explanation: 7/-3 = truncate(-2.33333..) = -2.
# Example 3:
#
# Input: dividend = 0, divisor = 1
# Output: 0
# Example 4:
#
# Input: dividend = 1, divisor = 1
# Output: 1
#
#
# Constraints:
#
# -2^31 <= dividend, divisor <= 2^31 - 1
# divisor != 0

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # we use bit manipulations

        # the basic idea is to subtract divisor from the dividend
        # but only subtract 1*divisor from dividend is inefficient
        # we should subtract multi-times of divisor from dividend by bit manipulation
        # for example, divisor<<1 becomes 2*divisor

        # check whether the quotient is positive

        # the only overflow is when dividend=INT_MIN and divisor=-1
        if dividend == -2 ** 31 and divisor == -1:
            return 2 ** 31 - 1
        pos = (dividend > 0) == (divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0

        while dividend >= divisor:
            multi_divisor = divisor  # start from 1*divisor, also happens when divisor <= dividend < multi_divisor
            increment = 1  # this is to record how many times of divisor we subtract from dividend each time
            while dividend >= multi_divisor:
                dividend -= multi_divisor
                quotient += increment
                multi_divisor = multi_divisor << 1  # double it
                increment = increment << 1
        return quotient if pos else -quotient


print(Solution().divide(10, 3))

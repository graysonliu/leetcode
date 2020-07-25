# Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.
#
# Return the quotient after dividing dividend by divisor.
#
# The integer division should truncate toward zero.
#
# Example 1:
#
# Input: dividend = 10, divisor = 3
# Output: 3
# Example 2:
#
# Input: dividend = 7, divisor = -3
# Output: -2
# Note:
#
# Both dividend and divisor will be 32-bit signed integers.
# The divisor will never be 0.
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1].
# For the purpose of this problem, assume that your function returns 2^31 − 1 when the division result overflows.

class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # 回忆一下C和Python中整除的区别，C中的整除向零取整，Python中的整除向负无穷取整
        # 正常的思路很简单，被除数不断减去除数即可
        # 但当除数很小（比如除数为1），而被除数又很大时，每次减一个除数太慢了

        # 首先确定商的符号
        positive = (dividend > 0) == (divisor > 0)

        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0

        while dividend >= divisor:
            multi_divisor, increment_quot = divisor, 1
            while dividend >= multi_divisor:
                dividend -= multi_divisor
                quotient += increment_quot
                # 移位操作，每次减的除数翻倍，所以商的增量也翻倍
                multi_divisor <<= 1  # 这里是每次左移一位，即每次乘2，每次左移更多位数其实也可以
                increment_quot <<= 1

        if not positive:
            quotient = -quotient

        inf = 2 ** 31
        return quotient if -inf <= quotient <= inf - 1 else inf - 1


if __name__ == "__main__":
    print(Solution().divide(10, 3))

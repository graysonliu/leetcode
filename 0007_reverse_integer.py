# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
# Input: 123
# Output: 321
# Example 2:
#
# Input: -123
# Output: -321
# Example 3:
#
# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

class Solution:
    def reverse(self, x: int) -> int:
        neg, x = (True, -x) if x < 0 else (False, x)
        res = 0
        while x != 0:
            x, digit = divmod(x, 10)
            res = res * 10 + digit
        res = -res if neg else res
        return res if -2 ** 31 <= res < 2 ** 31 else 0  # note that Python can handle infinite integer

    # about divmod() in Python
    # when dividing numbers, other languages like Java, C++ round the result towards 0 when the result is negative
    # but Python round the result towards negative infinite
    # for example, in Java/C++, 5/-2=-2, -5/2=-2, 5%-2=1, -5%2=-1
    # but in Python, 5//-2=-3, -5//2=-3, 5%-2=-1, -5%2=1, divmod(5,-2)=-3,-1, divmod(-5,2)=-3,1
    # to achieve the same dividing behaviour in Python, int(5/-2)=-2, int(-5/2)=-2
    # mod=5-(-2)*int(5/-2)=1, mod=-5-2*int(-5/2)=-1
    pass


print(Solution().reverse(-10))

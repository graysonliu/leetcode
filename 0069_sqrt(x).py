# Implement int sqrt(int x).
#
# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
#
# Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
#
# Example 1:
#
# Input: 4
# Output: 2
# Example 2:
#
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since
#              the decimal part is truncated, 2 is returned.

class Solution:
    def mySqrt(self, x: int) -> int:
        # binary search
        # search range: [0, ceil(x/2)]
        import math
        left, right = 0, math.ceil(x / 2)
        while left <= right:
            mid = left + (right - left) // 2
            if mid == 0 or mid <= x / mid:
                if (mid + 1) > x / (mid + 1):
                    return mid
                else:
                    left = mid + 1
            else:
                right = mid - 1


print(Solution().mySqrt(4))

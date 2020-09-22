# Given a positive integer num, write a function which returns True if num is a perfect square else False.
#
# Follow up: Do not use any built-in library function such as sqrt.
#
#
#
# Example 1:
#
# Input: num = 16
# Output: true
# Example 2:
#
# Input: num = 14
# Output: false
#
#
# Constraints:
#
# 1 <= num <= 2^31 - 1

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # using binary search similar to #0069
        # search range: 0 ~ num//2+1
        # since mid will be a divisor later, it cannot be 0
        # thus, we single out the situation when num=0
        if num == 0:
            return True
        left, right = 1, num // 2 + 1
        while left <= right:
            mid = left + (right - left) // 2
            if mid == num / mid:
                return True
            elif mid < num / mid:
                if mid + 1 > num / (mid + 1):
                    return False
                else:
                    left = mid + 1
            elif mid > num / mid:
                if mid - 1 < num / (mid - 1):
                    return False
                else:
                    right = mid - 1
        pass

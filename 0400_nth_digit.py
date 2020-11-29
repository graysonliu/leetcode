# Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...
#
# Note:
# n is positive and will fit within the range of a 32-bit signed integer (n < 2^31).
#
# Example 1:
#
# Input:
# 3
#
# Output:
# 3
# Example 2:
#
# Input:
# 11
#
# Output:
# 0
#
# Explanation:
# The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.

class Solution:
    def findNthDigit(self, n: int) -> int:
        # 1-digit number: 1 ~ 9, 9 digits in total
        # 2-digit number: 10 ~ 99, 90*2 digits in total
        # 3-digit number: 100 ~ 999, 900*3 digits in total
        # ...
        # i-digit number: 10^(i-1) ~ 10^i-1, 9*10^(i-1)*i digits in total

        i = 1
        while n >= 9 * 10 ** (i - 1) * i:
            n -= 9 * 10 ** (i - 1) * i
            i += 1
        if n == 0:  # nth digit is the last digit of the last (i-1)-digit number
            return int(str(10 ** (i - 1) - 1)[-1])
        quotient, remainder = divmod(n - 1, i)
        num = 10 ** (i - 1) + quotient
        return int(str(num)[remainder])


print(Solution().findNthDigit(13))

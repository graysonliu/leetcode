# Write a program to find the n-th ugly number.
#
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
#
# Example:
#
# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
# Note:
#
# 1 is typically treated as an ugly number.
# n does not exceed 1690.

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # The ugly-number sequence is 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, …
        # split the sequence to three groups:
        # (1) 1×2, 2×2, 3×2, 4×2, 5×2, …
        # (2) 1×3, 2×3, 3×3, 4×3, 5×3, …
        # (3) 1×5, 2×5, 3×5, 4×5, 5×5, …
        ugly_nums = [1]
        i = 1
        i2, i3, i5 = 0, 0, 0  # indices of ugly_nums
        while i < n:
            # the (i+1)th ugly number
            num = min(2 * ugly_nums[i2], 3 * ugly_nums[i3], 5 * ugly_nums[i5])
            if num == 2 * ugly_nums[i2]:
                i2 += 1
            if num == 3 * ugly_nums[i3]:
                i3 += 1
            if num == 5 * ugly_nums[i5]:
                i5 += 1
            ugly_nums.append(num)
            i += 1
        return ugly_nums[-1]

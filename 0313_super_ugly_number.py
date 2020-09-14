# Write a program to find the nth super ugly number.
#
# Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k.
#
# Example:
#
# Input: n = 12, primes = [2,7,13,19]
# Output: 32
# Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 super ugly numbers given primes = [2,7,13,19] of size 4.
# Note:
#
# 1 is a super ugly number for any given primes.
# The given numbers in primes are in ascending order.
# 0 < k ≤ 100, 0 < n ≤ 10^6, 0 < primes[i] < 1000.
# The nth super ugly number is guaranteed to fit in a 32-bit signed integer.

from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        # the same idea as #0264
        ugly_nums = [1]
        counts = [0] * len(primes)
        for _ in range(1, n):
            min_value, min_index = float('inf'), []
            for i in range(len(primes)):
                candidate = primes[i] * ugly_nums[counts[i]]
                if candidate < min_value:
                    min_value = candidate
                    min_index = [i]
                elif candidate == min_value:
                    min_index.append(i)
            ugly_nums.append(min_value)
            for i in min_index:
                counts[i] += 1
        return ugly_nums[-1]


print(Solution().nthSuperUglyNumber(n=12, primes=[2, 7, 13, 19]))

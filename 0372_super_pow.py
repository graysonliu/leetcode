# Your task is to calculate a^b mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.
#
# Example 1:
#
# Input: a = 2, b = [3]
# Output: 8
# Example 2:
#
# Input: a = 2, b = [1,0]
# Output: 1024

from typing import List


class Solution:
    def atMostTenPow(self, n, m):  # calculate n^m % 1337, 0<=m<=10
        res = 1
        for _ in range(m):
            res = (res * n) % 1337
        return res

    def superPow(self, a: int, b: List[int]) -> int:
        # a^1234567 % k = [(a^1234560 % k) * (a^7 % k)] %k = [((a^123456)^10 % k) * (a^7 % k)] %k
        # =[(a^123456 % k)^10 * (a^7 % k)] %k
        # superPow(a,b) = (superPow(a,b[:-1])**10 * superPow(a,b[-1])) % k  --> recursive
        if not b:
            return 1
        if len(b) == 1:
            return self.atMostTenPow(a, b[0])
        return (self.atMostTenPow(self.superPow(a, b[:-1]), 10) * self.superPow(a, [b[-1]])) % 1337


print(Solution().superPow(2, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))

# Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.
#
# Example 1:
#
# Input: 2
# Output: [0,1,1]
# Example 2:
#
# Input: 5
# Output: [0,1,1,2,1,2]
# Follow up:
#
# It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
# Space complexity should be O(n).
# Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        # 0:    0
        # 1:    1
        # 2~3:  1 2
        # 4~7:  1 2 2 3
        # 8~15: 1 2 2 3 2 3 3 4
        # ...
        # 2^(n-1)~2^n-1: [a, b, c,...]
        # 2^n~2^(n+1)-1: [a, b, c,..., a+1, b+1, c+1,...]
        if num == 0:
            return [0]
        res = [0, 1]
        lo, hi = 1, 2
        while hi <= num:
            res.extend(res[lo:hi])
            res.extend([i + 1 for i in res[lo:hi]])
            lo, hi = hi, 2 * hi
        return res[:num + 1]

        # another solution
        # f[i] = f[i // 2] + i % 2
        res = [0] * (num + 1)
        for i in range(num + 1):
            res[i] = res[i >> 1] + (i & 1)
        return res


print(Solution().countBits(5))

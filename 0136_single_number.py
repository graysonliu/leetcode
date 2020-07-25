# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#
# Example 1:
#
# Input: [2,2,1]
# Output: 1
# Example 2:
#
# Input: [4,1,2,1,2]
# Output: 4

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # trick: using xor
        # [4, 1, 2, 1, 2]: (1^1)^(2^2)^(4)=0^0^4=0^4=4
        from functools import reduce
        return reduce(lambda x, y: x ^ y, nums)

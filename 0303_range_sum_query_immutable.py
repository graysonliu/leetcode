# Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
#
# Example:
#
# Given nums = [-2, 0, 3, -5, 2, -1]
#
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
#
#
# Constraints:
#
# You may assume that the array does not change.
# There are many calls to sumRange function.
# 0 <= nums.length <= 10^4
# -10^5 <= nums[i] <= 10^5
# 0 <= i <= j < nums.length

from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            self.sums[i] = self.sums[i - 1] + nums[i - 1]

    def sumRange(self, i: int, j: int) -> int:
        return self.sums[j + 1] - self.sums[i]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

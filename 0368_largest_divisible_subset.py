# Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:
#
# Si % Sj = 0 or Sj % Si = 0.
#
# If there are multiple solutions, return any subset is fine.
#
# Example 1:
#
# Input: [1,2,3]
# Output: [1,2] (of course, [1,3] will also be ok)
# Example 2:
#
# Input: [1,2,4,8]
# Output: [1,2,4,8]
from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        res = []
        nums.sort()  # sort first
        dp_length = [1] * len(nums)  # dp[i] records information for subset end with nums[i]
        dp_subset = [[nums[i]] for i in range(len(nums))]
        for i in range(len(nums)):
            max_length_j = None
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp_length[j] + 1 > dp_length[i]:
                    max_length_j = j
                    dp_length[i] = dp_length[j] + 1
            if max_length_j is not None:
                dp_subset[i] = dp_subset[max_length_j] + [nums[i]]
            if dp_length[i] > len(res):
                res = dp_subset[i]
        return res


print(Solution().largestDivisibleSubset([1, 2, 3]))

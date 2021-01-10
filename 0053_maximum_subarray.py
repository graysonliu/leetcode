# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#
# Example:
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:
#
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # DP
        # dp[i] is the max summation of any subarrays that end with item nums[i]
        # then, we have dp[i] = max(dp[i-1] + nums[i], nums[i])
        dp = nums.copy()  # assign nums[i] to dp[i]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i], dp[i - 1] + nums[i])

        return max(dp)


print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

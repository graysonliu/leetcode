# Given an unsorted array of integers, find the length of longest increasing subsequence.
#
# Example:
#
# Input: [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Note:
#
# There may be more than one LIS combination, it is only necessary for you to return the length.
# Your algorithm should run in O(n2) complexity.
# Follow up: Could you improve it to O(n log n) time complexity?
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # these subsequence problems are usually solved by dynamic programming
        # for any subsequence end with nums[i],
        # if nums[i]>nums[j] (0<=j<=i-1), one candidate length is dp[j]+1,
        # the value of dp[i] is the maximum of all candidates
        if len(nums) == 0:
            return 0
        dp = [1] * len(nums)  # a single element subsequence has the length of 1
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
        # the algorithm above is of O(n^2) time complexity
        # note: there is a tricky O(nlogn) solution, see 4th approach in Leetcode's official solution

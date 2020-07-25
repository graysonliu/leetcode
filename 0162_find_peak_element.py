# A peak element is an element that is greater than its neighbors.
#
# Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.
#
# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
#
# You may imagine that nums[-1] = nums[n] = -∞.
#
# Example 1:
#
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.
# Example 2:
#
# Input: nums = [1,2,1,3,5,6,4]
# Output: 1 or 5
# Explanation: Your function can return either index number 1 where the peak element is 2,
#              or index number 5 where the peak element is 6.
# Follow up: Your solution should be in logarithmic complexity.

from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # a variant of binary search
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            # since mid==right only happens when left==right, however, left<right, we have mid<right, nums[mid+1] exists
            if nums[mid] < nums[mid + 1]:  # peak exists in [mid+1:]
                left = mid + 1
            else:  # nums[mid] > nums[mid+1], since nums[i] ≠ nums[i+1], peak exists in [0,mid]
                right = mid
        return left  # left==right

# Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....
#
# Example 1:
#
# Input: nums = [1, 5, 1, 1, 6, 4]
# Output: One possible answer is [1, 4, 1, 5, 1, 6].
# Example 2:
#
# Input: nums = [1, 3, 2, 2, 3, 1]
# Output: One possible answer is [2, 3, 1, 3, 1, 2].
# Note:
# You may assume all input has valid answer.
#
# Follow Up:
# Can you do it in O(n) time and/or in-place with O(1) extra space?

from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        import math
        half = math.ceil(len(nums) / 2)
        # then, we halve the sorted list to two parts
        half1, half2 = nums[:half], nums[half:]
        # any number in half2 is no less than any number in half1
        # merge those two halves alternately
        # but we need them reversed first
        # the reason is, for example, we have [1,2,2,3]
        # the first half would be [1,2], the second half would be [2,3]
        # merge if not reversed: [1,2,2,3]
        # merge if reversed: [2,3,1,2]
        nums[::2], nums[1::2] = half1[::-1], half2[::-1]

        # a better O(n) time with O(1) space solution:
        # https://leetcode.com/problems/wiggle-sort-ii/discuss/77677/O(n)%2BO(1)-after-median-Virtual-Indexing

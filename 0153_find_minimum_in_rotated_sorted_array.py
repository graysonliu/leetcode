# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
#
# Find the minimum element.
#
# You may assume no duplicate exists in the array.
#
# Example 1:
#
# Input: [3,4,5,1,2]
# Output: 1
# Example 2:
#
# Input: [4,5,6,7,0,1,2]
# Output: 0

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] <= nums[right]:  # [left, right] is in sorted order
                return nums[left]
            mid = left + (right - left) // 2
            # then, we must have nums[left]>nums[right]
            # nums[left] is definitely not the min value since at least nums[right] is less than it
            if nums[left] > nums[mid]:
                right = mid
                # if mid==right, then interval [left, right] will not shrink
                # however, interval [left, right] definitely shrinks since only when left==right we have mid==right
                # if left==right, the loop has already terminated since we returned nums[left] in the previous line
            else:
                left = mid + 1


print(Solution().findMin([2, 1]))

# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
#
# You are given a target value to search. If found in the array return true, otherwise return false.
#
# Example 1:
#
# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
# Example 2:
#
# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false
#
# Follow up:
#
# This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
# Would this affect the run-time complexity? How and why?
from typing import List


class Solution:
    # similar to #33
    # a variation of binary search
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            # rethink
            # between [left, mid-1] and [mid+1, right], one of them must be in sorted order
            # how to figure out which one is in sorted order?
            # if there are no duplicates in the list, we can easily find that out
            # if nums[mid]>nums[left], then [left, mid-1] is in sorted order
            # if nums[mid]<nums[left], then [mid+1, right] is in sorted order
            # when nums[mid]==nums[left], we know that mid==left and mid+1==right, this is the trivial case
            # [left, mid-1] is empty, therefore we just need to consider [mid+1, right], which only has one element
            # in this question, we have duplicates
            # we have to handle the situation when nums[mid]==nums[left] and [left, mid-1] is not empty
            # when nums[mid]==nums[left], if [left, mid-1] is sorted
            # then all numbers in [left, mid-1] should be the same
            # otherwise, [left, mid-1] is not sorted, [mid+1, right] is sorted instead
            while left < mid and nums[mid] == nums[left]:
                left += 1
            # note: we put left<mid in the cycle condition to make sure left<=mid<=right still holds
            # after exiting the above while cycle, we have either left=mid or nums[mid] != nums[left]
            if left == mid:
                left = mid + 1
            # since nums[mid] != nums[left], we can go back to our original strategy
            elif nums[mid] > nums[left]:
                if nums[left] <= target <= nums[mid - 1]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < nums[left]:
                if nums[mid + 1] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False


print(Solution().search([0, 0, 1, 1, 2, 0], 2))

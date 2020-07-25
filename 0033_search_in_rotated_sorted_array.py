# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
#
# You are given a target value to search. If found in the array return its index, otherwise return -1.
#
# You may assume no duplicate exists in the array.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# Example 1:
#
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
#
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

from typing import List


class Solution:
    # a variation of binary search
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            # between [left, mid-1] and [mid+1, right], one of them must be in sorted order
            # how to figure out which one is in sorted order?
            # since there are no duplicates in the list, we can easily find that out
            # if nums[mid]>nums[left], then [left, mid-1] is in sorted order
            # if nums[mid]<nums[left], then [mid+1, right] is in sorted order
            # when nums[mid]==nums[left], we know that mid==left and mid+1==right, this is the trivial case
            # [left, mid-1] is empty, therefore we just need to consider [mid+1, right], which only has one element
            if nums[mid] == nums[left]:
                left = mid + 1
            elif nums[mid] > nums[left]:  # [left, mid-1] is in sorted order
                if nums[left] <= target <= nums[mid - 1]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < nums[left]:  # [mid+1, right] is in sorted order
                if nums[mid + 1] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


if __name__ == "__main__":
    print(Solution().search([1, 3], 3))

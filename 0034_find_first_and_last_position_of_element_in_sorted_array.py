# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# Example 1:
#
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
#
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

from typing import List


class Solution:
    # binary search, the leftmost version and the rightmost version
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search_left_boundary():
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
            if left > len(nums) - 1 or nums[left] != target:
                return -1
            return left

        def binary_search_right_boundary():
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
            if right < 0 or nums[right] != target:
                return -1
            return right

        return [binary_search_left_boundary(), binary_search_right_boundary()]


if __name__ == "__main__":
    print(Solution().searchRange([5, 7, 7, 8, 8, 10], 6))

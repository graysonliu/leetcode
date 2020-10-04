# Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
#
# Notice that the solution set must not contain duplicate quadruplets.
#
#
#
# Example 1:
#
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# Example 2:
#
# Input: nums = [], target = 0
# Output: []
#
#
# Constraints:
#
# 0 <= nums.length <= 200
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # we adopt a solution similar to #0016
        # for any k-sum problem, this solution is O(n^(k-1))

        # sort first
        nums.sort()
        n = len(nums)
        res = []

        def increase_left(left, right):
            # increase left, and skip duplicates
            while left < right:
                left += 1
                if nums[left] != nums[left - 1]:
                    break
            return left

        def decrease_right(left, right):
            # decrease right, and skip duplicates
            while left < right:
                right -= 1
                if nums[right] != nums[right + 1]:
                    break
            return right

        def k_sum(k, start, target, combination):
            if k == 2:
                # using two pointers, which is O(n)
                left, right = start, n - 1
                while left < right:
                    s = nums[left] + nums[right]
                    if s == target:
                        res.append(combination + [nums[left], nums[right]])
                        left, right = increase_left(left, right), decrease_right(left, right)
                    elif s < target:
                        left = increase_left(left, right)
                    elif s > target:
                        right = decrease_right(left, right)
            else:
                i = start
                while i < n - k + 1:
                    # early termination
                    if sum(nums[i:i + k]) > target or sum(nums[n - k:n]) < target:
                        return
                    combination.append(nums[i])
                    k_sum(k - 1, i + 1, target - nums[i], combination)
                    combination.pop()
                    i = increase_left(i, n - k + 1)  # we also need to skip duplicates

        k_sum(4, 0, target, [])
        return res


print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))

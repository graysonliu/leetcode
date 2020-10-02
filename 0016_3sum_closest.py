# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
#
#
#
# Example 1:
#
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
#
#
# Constraints:
#
# 3 <= nums.length <= 10^3
# -10^3 <= nums[i] <= 10^3
# -10^4 <= target <= 10^4
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()  # sort first
        # we take each nums[i] as the first number of the triple
        # use two pointers
        # pointer left points to the possible 2nd number nums[left], it starts at i+1 following nums[i]
        # pointer right points to the possible 3rd number nums[right], it starts at len(nums)-1, the end of the list
        # if nums[i]+nums[left]+nums[right] is larger than target, we should decrease the sum by right-=1
        # otherwise, we should increase the sum by left+=1
        diff = float('inf')
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if abs(s - target) < abs(diff):
                    diff = s - target
                if s > target:
                    right -= 1
                else:
                    left += 1
        return target + diff
        # time complexity: O(n^2)


print(Solution().threeSumClosest([1, 2, 4, 8, 16, 32, 64, 128], 82))

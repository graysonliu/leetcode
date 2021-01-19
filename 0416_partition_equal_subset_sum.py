# Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.


# Example 1:

# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# Example 2:

# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.


# Constraints:

# 1 <= nums.length <= 200
# 1 <= nums[i] <= 100

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # subset problem
        # assume S is the summation of all items in the array
        # this problem actually asks whether there exists a subset whose summation is S/2
        # dynamic programming
        memo = {}

        # consider nums[0...i], whether there exists a subset of nums[0...i], which has a summation of target
        def dp(i, target):
            # no number left in nums[0...i], we have a solution only if target equals to 0
            if i < 0:
                return target == 0
            if (i, target) in memo:
                return memo[(i, target)]
            # for any nums[i], we either put it into the subset, or not
            memo[(i, target)] = dp(
                i - 1, target - nums[i]) or dp(i - 1, target)
            return memo[(i, target)]

        S = sum(nums)
        if S % 2 == 1:
            return False
        return dp(len(nums) - 1, S // 2)


print(Solution().canPartition([1, 2, 3, 5]))

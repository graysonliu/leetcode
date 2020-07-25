# Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.
#
# Example 1:
#
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:
#
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # this problem is similar to #53, which requires the max sum of subarray
        current_max = nums[0]  # this is the max product of all subarrays that end with nums[i]
        # due to the property of multiply, we also need to record the min product
        current_min = nums[0]
        best_max = nums[0]
        funcs = [max, min]
        for num in nums[1:]:
            current_max, current_min = [f(current_max * num, current_min * num, num) for f in funcs]
            best_max = max(best_max, current_max)
        return best_max


print(Solution().maxProduct([2, 3, -2, 4]))

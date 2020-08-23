# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
#
# Example:
#
# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.
#
# Note: Please solve it without division and in O(n).
#
# Follow up:
# Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # L = [1] * len(nums)  # L[i] is the product of all elements to the left of nums[i], L[0]=1
        # R = [1] * len(nums)  # R[i] is the product of all elements to the right of nums[i], R[len-1]=1
        # for i in range(1, len(L)):
        #     L[i] = L[i - 1] * nums[i - 1]
        # for i in range(len(R) - 2, -1, -1):
        #     R[i] = R[i + 1] * nums[i + 1]
        # return [L[i] * R[i] for i in range(0, len(nums))]

        # O(1) space complexity (note that output array does not count for space complexity)
        # construct one list of L and R first, then construct the other one on the fly

        res = [1] * len(nums)
        # construct L, similar to the previous solution
        for i in range(1, len(res)):
            res[i] = res[i - 1] * nums[i - 1]
        # construct R on the fly
        r = 1
        for i in range(len(res) - 2, -1, -1):
            r *= nums[i + 1]
            res[i] *= r
        return res

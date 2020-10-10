# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
#
# If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).
#
# The replacement must be in place and use only constant extra memory.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3]
# Output: [1,3,2]
# Example 2:
#
# Input: nums = [3,2,1]
# Output: [1,2,3]
# Example 3:
#
# Input: nums = [1,1,5]
# Output: [1,5,1]
# Example 4:
#
# Input: nums = [1]
# Output: [1]
#
#
# Constraints:
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [... m, ... n, ...]
        # next permutation should be larger than current permutation
        # we should swap a pair of numbers (m, n) that satisfy m<n and m is to the left of n, so that after the swapping, the permutation is larger
        # we also need to guarantee that after the swapping we get the smallest possible permutation that is larger than current permutation, which is the definition of 'next'
        # so, we look for this pair (m, n) for the right to the left
        # from right to left, we need to find the first number satisfying that there exists another number on its right that is larger than it
        # that first number is the m we want
        maximum = -float('inf')
        m = None
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < maximum:
                m = i  # m is the index rather than the actual number
                break
            else:
                maximum = nums[i]
        # if we think it thoroughly, this can also be achieve by find the first number that is smaller than the adjacent number on its right from the right to the left

        # then, we need to find n, n should be the smallest number that is larger than m on its right
        # maximum is the largest number on m's right, but maximum is not necessarily n
        # there could be another number on m's right and it is larger than m but smaller than maximum
        # since m is the first number that is smaller than some number on its right
        # all numbers on m's right is actually in a descending order
        # therefore, we search n from the right to the left, meaning we start from the smallest
        # the first number that we encounter and larger than m is the number n we want
        if m is not None:
            for i in range(len(nums) - 1, m, -1):
                if nums[i] > nums[m]:
                    n = i
                    break
            # swap
            nums[m], nums[n] = nums[n], nums[m]

        # after the swapping, it is still not done yet
        # the permutation becomes [... n, ... m, ...] and all numbers on n's right are in a descending order
        # to get the smallest next permutation, we should reverse all numbers on n's right, that is nums[n+1:]
        # if such (m, n) dose not exist, meaning the current permutation is already the largest permutation, we should reverse the whole list
        lo, hi = m + 1 if m is not None else 0, len(nums) - 1
        # m is the index, current nums[m] is actually nums[n] before the swapping
        while lo < hi:
            nums[lo], nums[hi] = nums[hi], nums[lo]
            lo, hi = lo + 1, hi - 1


Solution().nextPermutation([1, 3, 2])

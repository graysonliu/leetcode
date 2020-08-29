# Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.
#
# Example 1:
#
# Input: [1,3,4,2,2]
# Output: 2
# Example 2:
#
# Input: [3,1,3,4,2]
# Output: 3
# Note:
#
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n^2).
# There is only one duplicate number in the array, but it could be repeated more than once.

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # n = len(nums) - 1
        # the range of indices: 0~n
        # the range of values: 1~n
        # we construct a linked list, ...->A->B->..., if the value of A is k, then the value of B should be nums[k]
        # that is, the value of the previous node becomes the index of the value in the list of the next node
        # since we have the duplicate, the constructed linked list must have a cycle
        # example: https://leetcode.com/problems/find-the-duplicate-number/Figures/287/complex_cycle.png
        # the entrance of the cycle is the duplicate
        # thus, we converted this problem to #0142: finding the entrance of the cycle in a linked list
        fast, slow = nums[0], nums[0]
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break

        # we found the meeting node, then we should find the entrance of the cycle
        fast = nums[0]
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]

        return fast


print(Solution().findDuplicate([1, 3, 4, 2, 2]))

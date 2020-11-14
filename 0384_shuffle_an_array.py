# Given an integer array nums, design an algorithm to randomly shuffle the array.
#
# Implement the Solution class:
#
# Solution(int[] nums) Initializes the object with the integer array nums.
# int[] reset() Resets the array to its original configuration and returns it.
# int[] shuffle() Returns a random shuffling of the array.
#
#
# Example 1:
#
# Input
# ["Solution", "shuffle", "reset", "shuffle"]
# [[[1, 2, 3]], [], [], []]
# Output
# [null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]
#
# Explanation
# Solution solution = new Solution([1, 2, 3]);
# solution.shuffle();    // Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must be equally likely to be returned. Example: return [3, 1, 2]
# solution.reset();      // Resets the array back to its original configuration [1,2,3]. Return [1, 2, 3]
# solution.shuffle();    // Returns the random shuffling of array [1,2,3]. Example: return [1, 3, 2]
#
#
#
# Constraints:
#
# 1 <= nums.length <= 200
# -10^6 <= nums[i] <= 10^6
# All the elements of nums are unique.
# At most 5 * 10^4 calls will be made to reset and shuffle.

from typing import List
import random


class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums
        self.shuffled = self.original[:]

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.shuffled = self.original[:]
        return self.shuffled

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        # we determine elements of shuffled array one by one
        # for index i, elements of 0~(i-1) have already been confirmed, we find the value of index i from range i~(n-1)
        # we choose an element from range i~(n-1) randomly, then swap it with the element at index i
        n = len(self.shuffled)
        for i in range(n):
            j = random.randrange(i, n)
            self.shuffled[i], self.shuffled[j] = self.shuffled[j], self.shuffled[i]
        return self.shuffled

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

# Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.
#
# Follow up: Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
#
# Example 1:
#
# Input: nums = [1,2,1,3,2,5]
# Output: [3,5]
# Explanation:  [5, 3] is also a valid answer.
#
# Example 2:
#
# Input: nums = [-1,0]
# Output: [-1,0]
#
# Example 3:
#
# Input: nums = [0,1]
# Output: [1,0]
#
# Constraints:
#
# 1 <= nums.length <= 30000
# Each integer in nums will appear twice, only two integers will appear once.

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d = {}
        res = []
        for num in nums:
            d[num] = d.get(num, 0) + 1
        for num in d:
            if d[num] == 1:
                res.append(num)
        return res

    # constant space complexity solution: https://leetcode.com/problems/single-number-iii/discuss/68900/Accepted-C%2B%2BJava-O(n)-time-O(1)-space-Easy-Solution-with-Detail-Explanations

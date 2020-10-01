# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Notice that the solution set must not contain duplicate triplets.
#
#
#
# Example 1:
#
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Example 2:
#
# Input: nums = []
# Output: []
# Example 3:
#
# Input: nums = [0]
# Output: []
#
#
# Constraints:
#
# 0 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # suppose [a,b,c] is a valid triple, and a<=b<=c
        # then, either a=b=c=0, or we must have a<0 and c>0
        res = []
        from collections import defaultdict
        count = defaultdict(int)
        pos, neg = set(), set()
        for num in nums:
            count[num] += 1
            pos.add(num) if num > 0 else (neg.add(num) if num != 0 else ())
        if 0 in count and count[0] >= 3:
            res.append([0, 0, 0])
        for a in neg:
            for c in pos:
                b = -a - c
                # remember that a<=b<=c, b should also be in count
                if b < a or b > c or b not in count:
                    continue
                # b is in count, but there are not enough b
                if (b == a or b == c) and count[b] < 2:
                    continue
                res.append([a, b, c])
        return res


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))

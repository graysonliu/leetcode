# Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.
#
# Example:
#
# nums = [1, 2, 3]
# target = 4
#
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
#
# Note that different sequences are counted as different combinations.
#
# Therefore the output is 7.
#
#
# Follow up:
# What if negative numbers are allowed in the given array?
# How does it change the problem?
# What limitation we need to add to the question to allow negative numbers?
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # my solution: (rejected because of timeout)
        # it's backtracking, to improve the performance, we treat combinations in different order as the same one
        # we achieve this by add numbers to the path from smallest to the largest
        # we also use count instead of path
        # when we get a valid count, we calculate the number of all combinations of this count
        from math import factorial
        nums.sort()
        self.res = 0

        def comb(n, k):
            return factorial(n) // (factorial(k) * factorial(n - k))

        def backtrack(count, start_index, target):
            if target == 0:
                c = 1
                values = count.values()
                n = sum(values)
                for k in values:
                    c = c * comb(n, k)
                    n = n - k
                self.res += c
                return

            for i in range(start_index, len(nums)):
                num = nums[i]
                if target - num >= 0:
                    count[num] += 1
                    backtrack(count, i, target - num)
                    count[num] -= 1
                else:
                    break

        from collections import defaultdict
        backtrack(defaultdict(int), 0, target)
        return self.res

        # a better accepted solution
        # imagine the last number of a valid combination is nums[i]
        # then, we have comb(target-nums[i]) combinations that satisfy this specific situation
        # so, we just have to add up all comb(target-nums[i]) for all nums[i]
        dp = [0] * (target + 1)
        dp[0] = 1  # no element in the combination, an empty combination is valid for target=0
        for i in range(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]
        return dp[target]

        pass


print(Solution().combinationSum4(
    [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250,
     260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480,
     490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710,
     720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940,
     950, 960, 970, 980, 990, 111]
    , 999))

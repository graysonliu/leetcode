from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # solution1: dfs
        # solution2: dfs with memory (dynamic programming)

        # easiest: greedy
        # find the leftmost element that could jump to the last element from end to start
        lastPos = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= lastPos:
                lastPos = i
        return lastPos == 0


print(Solution().canJump([2, 3, 1, 1, 4]))

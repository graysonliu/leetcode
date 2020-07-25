# Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
# Input: [1,2,2]
# Output:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # backtrack
        res = []
        nums.sort()

        def backtrack(path, candidates):
            res.append(path)
            if len(candidates) == 0:
                return
            for i in range(len(candidates)):
                if i == 0 or candidates[i] != candidates[i - 1]:
                    backtrack(path + [candidates[i]], candidates[i + 1:])

        backtrack([], nums)
        return res


print(Solution().subsetsWithDup([1, 2, 2]))

# Given a set of distinct integers, nums, return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # all integers in the set are distinct
        # dfs/backtracking
        res = []

        def dfs(subset, candidates):
            res.append(subset)
            for i in range(len(candidates)):
                dfs(subset + [candidates[i]], candidates[i + 1:])

        dfs([], nums)
        return res


print(Solution().subsets([1, 2, 3]))

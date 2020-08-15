# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
#
# Each number in candidates may only be used once in the combination.
#
# Note:
#
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:
#
# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
# Example 2:
#
# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
#   [1,2,2],
#   [5]
# ]

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        solutions = []

        candidates.sort()

        # compare this to #0039
        def backtrack(candidates, path, target):
            if target == 0:
                solutions.append(path)
                return
            elif target < 0:
                return
            if len(candidates) == 0:
                return
            for i, n in enumerate(candidates):
                if i == 0 or (n != candidates[i - 1]):
                    backtrack(candidates[i + 1:], path + [n], target - n)

        backtrack(candidates, [], target)
        return solutions


print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))

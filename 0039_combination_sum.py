# Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
#
# The same repeated number may be chosen from candidates unlimited number of times.
#
# Note:
#
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:
#
# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
#   [7],
#   [2,2,3]
# ]
# Example 2:
#
# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]

from typing import List


class Solution:
    # a variation of backtrack
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        solutions = []

        def backtrack(c, n, path):
            if n == 0:
                solutions.append(path)
                return
            elif n < 0:
                return
            for i, candidate in enumerate(c):
                backtrack(c[i:], n - candidate, path + [candidate])
                # candidates are from c[i:] rather than c, this is to remove duplicate solutions
                # for example, when target=5, [2, 3] and [3, 2] are same solutions
                # we always add the smallest candidate to the path first to solve this problem

        backtrack(candidates, target, [])
        return solutions


print(Solution().combinationSum([2, 3, 6, 7], 7))

# Given a collection of distinct integers, return all possible permutations.
#
# Example:
#
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []

        # backtrack
        def backtrack(path, candidates):
            if len(candidates) == 0:
                results.append(path)
                return
            for i, num in enumerate(candidates):
                candidates.pop(i)
                backtrack(path + [num], candidates)
                candidates.insert(i, num)

        backtrack([], nums)
        return results


print(Solution().permute([1, 2, 3]))

# Given a collection of numbers that might contain duplicates, return all possible unique permutations.
#
# Example:
#
# Input: [1,1,2]
# Output:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []

        def backtrack(path, candidates):
            if len(candidates) == 0:
                results.append(path)
                return
            selected = set()
            for i, num in enumerate(candidates):
                if num not in selected:
                    selected.add(num)
                    candidates.pop(i)
                    backtrack(path + [num], candidates)
                    candidates.insert(i, num)

        backtrack([], nums)
        return results


print(Solution().permuteUnique([1, 1, 2]))

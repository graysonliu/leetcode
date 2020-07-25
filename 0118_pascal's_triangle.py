# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it.
#
# Example:
#
# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # dynamic programming
        res = []
        if numRows == 0:
            return res
        res.append([1])
        for i in range(1, numRows):
            pre_level = res[i - 1]
            cur_level = [1]
            for j in range(1, len(pre_level)):
                cur_level.append(pre_level[j - 1] + pre_level[j])
            cur_level.append(1)
            res.append(cur_level)
        return res

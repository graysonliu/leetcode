# Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.
#
# Example 1:
#
# Input: "2-1-1"
# Output: [0, 2]
# Explanation:
# ((2-1)-1) = 0
# (2-(1-1)) = 2
# Example 2:
#
# Input: "2*3-4*5"
# Output: [-34, -14, -10, -10, 10]
# Explanation:
# (2*(3-(4*5))) = -34
# ((2*3)-(4*5)) = -14
# ((2*(3-4))*5) = -10
# (2*((3-4)*5)) = -10
# (((2*3)-4)*5) = 10

import re
from typing import List


class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        # dynamic programming
        dp = {}
        nums = []  # save all numbers
        ops = []  # save all operations
        num = 0
        for c in input:
            if c.isdigit():
                num = num * 10 + int(c)
            else:
                nums.append(num)
                num = 0
                ops.append(c)

        # the last number isn't put into the list in previous iteration
        nums.append(num)

        for i in range(len(nums)):
            # the result from ith number to ith number, only 1 number participates the calculation
            dp[(i, i)] = [nums[i]]

        for i in range(1, len(nums)):  # i+1 is the number of participating numbers
            for j in range(0, len(nums) - i):  # j is the index of the start of participating numbers
                dp[(j, j + i)] = []  # the result from jth number to (j+i)th number
                for k in range(j, j + i):  # k is the partition
                    half1, half2 = dp[(j, k)], dp[(k + 1, j + i)]
                    # get the operation after the kth number
                    op = ops[k]
                    for h1 in half1:
                        for h2 in half2:
                            if op == '+':
                                dp[(j, j + i)].append(h1 + h2)
                            elif op == '-':
                                dp[(j, j + i)].append(h1 - h2)
                            elif op == '*':
                                dp[(j, j + i)].append(h1 * h2)

        return dp[(0, len(nums) - 1)]


print(Solution().diffWaysToCompute("2*3-4*5"))

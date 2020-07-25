# Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
#
# Note that the row index starts from 0.
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it.
#
# Example:
#
# Input: 3
# Output: [1,3,3,1]
# Follow up:
#
# Could you optimize your algorithm to use only O(k) extra space?

from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # dynamic programming
        # we only need to know the previous row to confirm current row
        row = [1]
        for i in range(rowIndex):
            pre = row[0]
            for j in range(1, len(row)):
                temp = row[j]
                row[j] = pre + row[j]
                pre = temp
            row.append(1)
        return row


print(Solution().getRow(3))

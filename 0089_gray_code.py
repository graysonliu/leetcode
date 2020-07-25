# The gray code is a binary numeral system where two successive values differ in only one bit.
#
# Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.
#
# Example 1:
#
# Input: 2
# Output: [0,1,3,2]
# Explanation:
# 00 - 0
# 01 - 1
# 11 - 3
# 10 - 2
#
# For a given n, a gray code sequence may not be uniquely defined.
# For example, [0,2,3,1] is also a valid gray code sequence.
#
# 00 - 0
# 10 - 2
# 11 - 3
# 01 - 1
# Example 2:
#
# Input: 0
# Output: [0]
# Explanation: We define the gray code sequence to begin with 0.
#              A gray code sequence of n has size = 2^n, which for n = 0 the size is 2^0 = 1.
#              Therefore, for n = 0 the gray code sequence is [0].
from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        # dynamic programming
        # find the optimal substructure
        # n=1: [0, 1]
        # n=2: add 0 and 1 to the front respectively to the previous code set
        # we have [00, 01, 10, 11]
        # however, the second 01 and third 10 have two different bits
        # to solve this, after we add 0 to the front, before we add 1 to the front, we reverse the previous code set
        # then the two elements at the border will only have their highest bit different
        # note: adding 0 to the front will not change the value, therefore we only need to add 1 to the front reversely
        res = [0]
        for i in range(n):
            for j in range(len(res) - 1, -1, -1):
                res.append(res[j] | 1 << i)

        return res


print(Solution().grayCode(2))

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
#
#
# Example 1:
#
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:
#
# Input: n = 1
# Output: ["()"]
#
#
# Constraints:
#
# 1 <= n <= 8
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # adding parenthesis one by one
        # the opening parenthesis should always be no less than the closing parenthesis
        res = []

        def recurse(count_open, count_close, path):
            if len(path) == 2 * n:
                res.append(''.join(path))
                return
            if count_open < n:
                path.append('(')
                recurse(count_open + 1, count_close, path)
                path.pop()
            if count_close < count_open:
                path.append(')')
                recurse(count_open, count_close + 1, path)
                path.pop()

        recurse(0, 0, [])
        return res


print(Solution().generateParenthesis(3))

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

class Solution:

    # 思路：构建字符串的过程中左括号数量始终大于右括号即可
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        ans = []

        def append_recursively(s, left_count, right_count):  # 递归
            if len(s) == 2 * n:  # 长度够了，加入结果列表
                ans.append(s)
                return
            if left_count < n:
                append_recursively(s + '(', left_count + 1, right_count)
            if left_count > right_count:  # 保证左括号的数量始终大于右括号
                append_recursively(s + ')', left_count, right_count + 1)

        append_recursively('(', 1, 0)
        return ans

    # 思路：将问题分解
    """
    结果字符串可以被开头的左括号以及它所对应的右括号分为两部分，即({left}){right}
    而{left}和{right}中的括号顺序必然是合法的
    """

    def generateParenthesis1(self, n):
        ans = []
        if n == 0:  # 总长度为2*n
            return ['']
        for c in range(n):
            for left in self.generateParenthesis1(c):  # 左边部分长度为2*c
                for right in self.generateParenthesis1(n - 1 - c):  # 右边部分长度为2*n-2-2*c
                    ans.append('({}){}'.format(left, right))  # 左右两部分合并，保证总长度为2*n
        return ans


if __name__ == '__main__':
    print(Solution().generateParenthesis1(3))

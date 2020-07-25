# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.
#
# Example 1:
#
# Input: "()"
# Output: true
# Example 2:
#
# Input: "()[]{}"
# Output: true
# Example 3:
#
# Input: "(]"
# Output: false
# Example 4:
#
# Input: "([)]"
# Output: false
# Example 5:
#
# Input: "{[]}"
# Output: true

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 简单的栈管理，没什么好说的
        pair = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for c in s:
            if stack and pair.get(stack[-1], None) == c:
                stack.pop(-1)
            else:
                stack.append(c)
        return not stack


if __name__ == '__main__':
    print(list(map(Solution().isValid, ["()", "(]", "{[]}"])))

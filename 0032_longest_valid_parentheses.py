# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.


# Example 1:

# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".
# Example 2:

# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".
# Example 3:

# Input: s = ""
# Output: 0


# Constraints:

# 0 <= s.length <= 3 * 10^4
# s[i] is '(', or ')'.


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # for an one-dimensional DP problem
        # the trick is always to find the result if the valid sequence ends at index i
        # dp[i] = (the longest valid sequence that ends at s[i])

        stack = []
        dp = [0] * len(s)  # initialization
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif stack:  # pop from stack when it is ')' and when stack is not empty
                j = stack.pop()
                # s[j] is the '(' that matches the current ')'
                # i - j + 1 is the length from s[j] to s[i]
                # however, this might not be the longest valid sequence that ends at s[i]
                # because we can concatenate the longest valid sequence ending at s[j-1] with s[j]...s[i]
                dp[i] = i - j + 1 + (dp[j - 1] if j >= 1 else 0)

        return max(dp) if dp else 0


print(Solution().longestValidParentheses(")()())"))

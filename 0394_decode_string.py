# Given an encoded string, return its decoded string.
#
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
#
# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
#
# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].
#
#
#
# Example 1:
#
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# Example 2:
#
# Input: s = "3[a2[c]]"
# Output: "accaccacc"
# Example 3:
#
# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
# Example 4:
#
# Input: s = "abc3[cd]xyz"
# Output: "abccdcdcdxyz"
#
#
# Constraints:
#
# 1 <= s.length <= 30
# s consists of lowercase English letters, digits, and square brackets '[]'.
# s is guaranteed to be a valid input.
# All the integers in s are in the range [1, 300].

class Solution:
    def decodeString(self, s: str) -> str:
        res = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                repeat = 0
                while s[i] != '[':  # fetch all consecutive digits
                    repeat = 10 * repeat + int(s[i])
                    i += 1
                bracket = 1
                i += 1
                start = i
                while bracket != 0:  # match the right bracket
                    if s[i] == '[':
                        bracket += 1
                    elif s[i] == ']':
                        bracket -= 1
                    i += 1
                inside_brackets_decoded = self.decodeString(s[start:i - 1])
                for _ in range(repeat):
                    res.append(inside_brackets_decoded)
            else:
                res.append(s[i])
                i += 1

        return ''.join(res)

        # using stack
        num_stack = []
        string_stack = ['']
        cur_num = 0
        for c in s:
            if c.isdigit():
                cur_num = 10 * cur_num + int(c)
            elif c.isalpha():
                string_stack[-1] += c
            elif c == '[':  # push into the stack
                num_stack.append(cur_num)
                string_stack.append('')
                cur_num = 0
            elif c == ']':  # pop from the stack
                repeat = num_stack.pop()
                string_in_bracket = string_stack.pop()
                string_stack[-1] += repeat * string_in_bracket
        return string_stack[0]


print(Solution().decodeString("3[a]2[bc]"))

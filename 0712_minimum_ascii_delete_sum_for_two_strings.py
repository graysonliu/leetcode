# Given two strings s1, s2, find the lowest ASCII sum of deleted characters to make two strings equal.

# Example 1:
# Input: s1 = "sea", s2 = "eat"
# Output: 231
# Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
# Deleting "t" from "eat" adds 116 to the sum.
# At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
# Example 2:
# Input: s1 = "delete", s2 = "leet"
# Output: 403
# Explanation: Deleting "dee" from "delete" to turn the string into "let",
# adds 100[d]+101[e]+101[e] to the sum.  Deleting "e" from "leet" adds 101[e] to the sum.
# At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
# If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
# Note:

# 0 < s1.length, s2.length <= 1000.
# All elements of each string will have an ASCII value in [97, 122].

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # similar to #0583, but we have to calculate the ascii sum of deleted characters rather than the number of deleted characters

        memo = {}

        # compare s1[0...i] and s2[0...j]
        def dp(i, j):
            if i == -1:  # s1[0...i] is empty, delete all items in s2[0...j]
                return sum(map(ord, s2[0:j + 1]))
            if j == -1:  # similarly
                return sum(map(ord, s1[0:i + 1]))
            if (i, j) in memo:
                return memo[(i, j)]
            if s1[i] == s2[j]:
                memo[(i, j)] = dp(i - 1, j - 1)
            else:  # delete either s1[i] or s2[j]
                memo[(i, j)] = min(dp(i - 1, j) + ord(s1[i]),
                                   dp(i, j - 1) + ord(s2[j]))
            return memo[(i, j)]

        return dp(len(s1) - 1, len(s2) - 1)

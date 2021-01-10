# Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same, where in each step you can delete one character in either string.

# Example 1:
# Input: "sea", "eat"
# Output: 2
# Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
# Note:
# The length of given words won't exceed 500.
# Characters in given words can only be lower-case letters.

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # this is similar to #0072 Edit Distance
        memo = {}

        # compare word1[0...i] and word2[0...j]
        def dp(i, j):
            if i == -1:  # when word1[0...i] is empty
                # we have to delete all characters left in word2[0...j]
                return j + 1
            # similarly
            if j == -1:
                return i + 1
            if (i, j) in memo:
                return memo[(i, j)]
            if word1[i] != word2[j]:
                # delete either word1[i] or word2[j]
                memo[(i, j)] = min(dp(i - 1, j), dp(i, j - 1)) + 1
            else:  # no deleting
                memo[(i, j)] = dp(i - 1, j - 1)
            return memo[(i, j)]

        return dp(len(word1) - 1, len(word2) - 1)

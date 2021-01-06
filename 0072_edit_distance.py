# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

# You have the following three operations permitted on a word:

# Insert a character
# Delete a character
# Replace a character


# Example 1:

# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation:
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
# Example 2:

# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation:
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')


# Constraints:

# 0 <= word1.length, word2.length <= 500
# word1 and word2 consist of lowercase English letters.

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # this is a typical DP problem
        # when using DP, always think of what are states, what are the choices between state transfer
        # top-down, compare the last character of two strings, if they are not the same, we have three choices: insert, delete, replace

        memo = {}

        # compare word1[0...i] and word2[0...j]
        def dp(i, j):
            if i == -1:  # at the beginning of the first string, the second string still has j+1 characters to match
                return j + 1
            if j == -1:  # at the beginning of the second string
                return i + 1
            if (i, j) in memo:
                return memo[(i, j)]
            if word1[i] == word2[j]:  # the characters match, no action needed
                memo[(i, j)] = dp(i - 1, j - 1)
            else:  # we choose one of those three actions on the first string
                # insert on word1
                insert = dp(i, j - 1) + 1
                # delete on word1
                delete = dp(i - 1, j) + 1
                # replace on word1
                replace = dp(i - 1, j - 1) + 1
                memo[(i, j)] = min(insert, delete, replace)
            return memo[(i, j)]

        return dp(len(word1) - 1, len(word2) - 1)


print(Solution().minDistance('intention', 'execution'))

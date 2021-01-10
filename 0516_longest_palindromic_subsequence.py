# Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

# Example 1:
# Input:

# "bbbab"
# Output:
# 4
# One possible longest palindromic subsequence is "bbbb".


# Example 2:
# Input:

# "cbbd"
# Output:
# 2
# One possible longest palindromic subsequence is "bb".


# Constraints:

# 1 <= s.length <= 1000
# s consists only of lowercase English letters.

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # typical dynamic programming
        # for any substring that starts at index i, and ends at index j (i<=j)
        # the longest subsequence in this substring is dp[i][j]
        # then, if s[i]==s[j], dp[i][j]=dp[i+1][j-1]+2
        # if s[i]!=s[j], dp[i][j]=max(dp[i+1][j], dp[i][j-1])
        # we use recursion with memo
        memo = {}

        def dp(i, j):
            if i == j:  # single character
                return 1
            if i > j:
                return 0  # empty substring
            if (i, j) in memo:
                return memo[(i, j)]
            if s[i] == s[j]:
                memo[(i, j)] = dp(i + 1, j - 1) + 2
            else:
                memo[(i, j)] = max(dp(i + 1, j), dp(i, j - 1))
            return memo[(i, j)]

        return dp(0, len(s) - 1)


print(Solution().longestPalindromeSubseq('cbbd'))

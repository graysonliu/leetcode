# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
#
# Note:
#
# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.
# Example 1:
#
# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:
#
# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
#              Note that you are allowed to reuse a dictionary word.
# Example 3:
#
# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dynamic programming
        # optimal structure: s[0:a] is breakable if s[0:b] is breakable and s[b:a] is a word
        words = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True  # s[0:0], which is an empty string, is breakable
        length = len(words)
        for i in range(1, len(s) + 1):
            if i <= length:  # optimization
                for j in range(i - 1, -1, -1):  # iterate i times
                    if dp[j] and s[j:i] in words:
                        dp[i] = True
                        break
            else:
                for word in words:  # iterate len(words) times
                    if i - len(word) >= 0 and dp[i - len(word)] and s[i - len(word):i] == word:
                        dp[i] = True
                        break

        return dp[-1]


print(Solution().wordBreak(s="leetcode", wordDict=["leet", "code"]))

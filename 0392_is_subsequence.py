# Given a string s and a string t, check if s is subsequence of t.
#
# A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).
#
# Follow up:
#     If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?
#
# Credits:
# Special thanks to @pbrother for adding this problem and creating all test cases.
#
#
#
# Example 1:
#
# Input: s = "abc", t = "ahbgdc"
# Output: true
#
# Example 2:
#
# Input: s = "axc", t = "ahbgdc"
# Output: false
#
#
# Constraints:
#
# 0 <= s.length <= 100
# 0 <= t.length <= 10^4
# Both strings consists only of lowercase characters.

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        from collections import defaultdict
        mapping = defaultdict(list)
        for i, c in enumerate(t):
            mapping[c].append(i)

        p = -1  # current pointer on t

        # my version
        for c in s:
            # mapping[c] must have at least one element larger than p
            if c not in mapping or mapping[c][-1] <= p:  # mapping[c][-1] is the biggest index for c in t
                return False
            for i in mapping[c]:
                if i > p:
                    p = i
                    break
        return True

        # more concise version using bisect
        import bisect
        for c in s:
            j = bisect.bisect(mapping[c], p)  # bisect uses binary search, which is more efficient
            if j == len(mapping[c]):  # all indices of c in t are less than p
                return False
            p = mapping[c][j]
        return True

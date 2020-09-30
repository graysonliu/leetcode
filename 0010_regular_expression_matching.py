# Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
#
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).
#
# Note:
#
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like . or *.
# Example 1:
#
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:
#
# Input:
# s = "aa"
# p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
# Example 3:
#
# Input:
# s = "ab"
# p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
# Example 4:
#
# Input:
# s = "aab"
# p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
# Example 5:

#
# Input:
# s = "mississippi"
# p = "mis*is*p*."
# Output: false

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # intuitively, we can solve this problem by recursions
        # compare s and p for each character one by one from the start

        # optional: DP cache
        cache = {}

        def match(i, j):

            if (i, j) in cache:
                return cache[i, j]

            # this is to match s[i:] and p[j:]
            # use indices rather than slices of string each time, which can boost performance

            if j == len(p):  # we reach the end of p, p[j:] is empty
                cache[i, j] = i == len(s)  # if there is a match, s[i:] must also be empty
            else:
                # compare first character
                # if s[i:] is empty, first_match should be false
                first_matched = i != len(s) and (s[i] == p[j] or p[j] == '.')
                # if first characters do not match, s[i:] and p[j:] could still match if there is a '*' following p[j]

                # if there is a '*' following p[j]
                if j + 1 < len(p) and p[j + 1] == '*':
                    # two situations
                    # p[j] repeats zero times, then we can ignore p[j] and following '*', i->i, j->j+2
                    # p[j] repeats multiple times, in this case the first character must match, i->i+1, j->j
                    cache[i, j] = match(i, j + 2) or (first_matched and match(i + 1, j))

                # it the following character of p[j] is not '*', i->i+1, j->j+1
                else:
                    cache[i, j] = first_matched and match(i + 1, j + 1)

            return cache[i, j]

        return match(0, 0)


print(Solution().isMatch('aa', 'a*'))

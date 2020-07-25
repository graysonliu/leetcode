# Given a string s, partition s such that every substring of the partition is a palindrome.
#
# Return all possible palindrome partitioning of s.
#
# Example:
#
# Input: "aab"
# Output:
# [
#   ["aa","b"],
#   ["a","a","b"]
# ]

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        # d[i] saves the start and the end of all palindrome string that starts from i
        # s[start:end] is a palindrome string (s[end] is not included)
        d = [[] for _ in range(len(s))]

        for i in range(len(s)):
            d[i].append((i, i + 1))
            left, right = i - 1, i + 1
            # find consecutive same characters
            while right < len(s) and s[right] == s[i]:
                d[i].append((i, right + 1))
                right += 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                d[left].append((left, right + 1))
                left -= 1
                right += 1

        def find_partition(path, start):
            if start == len(s):
                res.append(path)
                return
            for (i, j) in d[start]:
                find_partition(path + [s[i:j]], j)

        find_partition([], 0)
        return res


print(Solution().partition('aab'))

# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:
#
# All given inputs are in lowercase letters a-z.
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # trick: use zip(*) to unzip a list of iterables
        # for example, list(zip(*[(1, 4), (2, 5), (3, 6)])) -> [(1, 2, 3), (4, 5, 6)]
        # list(zip(*["fl","fls"])) -> [('f', 'f'), ('l', 'l')]
        res = []
        for i, c in enumerate(zip(*strs)):
            if len(set(c)) == 1:
                res.append(c[0])
            else:
                break
        return ''.join(res)


print(Solution().longestCommonPrefix(["cfl", "fls"]))

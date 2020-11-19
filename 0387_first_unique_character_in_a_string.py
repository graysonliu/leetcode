# Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode"
# return 2.
#
#
# Note: You may assume the string contains only lowercase English letters.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # one pass solution
        letters = {}
        for i in range(ord('a'), ord('z') + 1):
            letters[chr(i)] = float('inf')
        for i, c in enumerate(s):
            if c not in letters:
                continue
            if letters[c] == float('inf'):  # meaning this letter never showed up before
                letters[c] = i
            else:  # we met this letter before, this letter is not unique
                letters.pop(c)
        if len(letters) == 0:  # all 26 letters showed up and all of them are not unique
            return -1
        res = min(letters.values())
        return res if res != float('inf') else -1

        # a clean two pass solution
        from collections import Counter
        count = Counter(s)
        for i, c in enumerate(s):
            if count[c] == 1:
                return i
        return -1


print(Solution().firstUniqChar("leetcode"))

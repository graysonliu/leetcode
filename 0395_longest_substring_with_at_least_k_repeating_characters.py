# Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.
#
# Example 1:
#
# Input:
# s = "aaabb", k = 3
#
# Output:
# 3
#
# The longest substring is "aaa", as 'a' is repeated 3 times.
# Example 2:
#
# Input:
# s = "ababbc", k = 2
#
# Output:
# 5
#
# The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if k <= 1:
            return len(s)
        res = 0
        from collections import defaultdict
        # we first count how many unique letters the string has
        unique_max = len(set(s))
        # therefore, for any substring, it can have at most unique_max unique letters
        # we check all possible numbers of unique letters for a substring
        for u in range(1, unique_max + 1):  # if the substring has exactly u unique letters
            # using a slide window
            window_unique = 0  # this is the the number of unique letters inside the sliding window
            left = 0
            right = -1
            count = defaultdict(int)
            while True:
                if window_unique <= u:  # expand the window on the right
                    if right == len(s) - 1:
                        break  # we cannot expand the window anymore
                    right += 1
                    c = s[right]
                    if count[c] == 0:
                        window_unique += 1
                    count[c] += 1
                else:  # shrink the window on the left
                    c = s[left]
                    if count[c] == 1:
                        window_unique -= 1
                    count[c] -= 1
                    left += 1
                if window_unique == u:
                    # check if all letters are counted at least k
                    # v==0 means this letter does not exist in the substring
                    if all([v == 0 or v >= k for v in count.values()]):
                        res = max(res, right - left + 1)

        return res


print(Solution().longestSubstring(s="aaabb", k=3))

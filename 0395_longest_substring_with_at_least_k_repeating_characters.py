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
        # similar to #0003, consider using slide window on substring problems
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
            while right + 1 < len(s):
                # we try to expand the slide window on the right
                # if s[right+1] not in count, but we already have u unique letters within the window
                # we cannot expand without shrinking first
                # because that would make the substring have more than u unique letters
                # we should shrink the slide window on the left
                # until the number of unique letters in the window is less than u
                if s[right + 1] not in count and len(count) == u:
                    while len(count) == u:
                        c = s[left]
                        count[c] -= 1
                        if count[c] == 0:
                            count.pop(c)
                        left += 1
                c = s[right + 1]
                count[c] += 1
                right += 1

                if len(count) == u:  # this substring should have exactly u unique letters
                    # check if all letters are counted at least k
                    if all([v >= k for v in count.values()]):
                        res = max(res, right - left + 1)

        return res


print(Solution().longestSubstring(s="ababbc", k=2))

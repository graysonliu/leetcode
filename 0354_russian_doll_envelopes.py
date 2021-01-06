# You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

# What is the maximum number of envelopes can you Russian doll? (put one inside other)

# Note:
# Rotation is not allowed.

# Example:

# Input: [[5,4],[6,4],[6,7],[2,3]]
# Output: 3
# Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).

from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # this problem can be actually converted to #300 Longest Increasing Subsequence
        # note that fitting one envelop into another requires strictly greater width and height
        # we first sort all envelopes by their width
        # then, if envelope A can be fitted into envelope B, A must be before B in the sorted array
        # to fit A into B, we also need to make sure that the height of A is strictly less than B
        # that is to find an increasing subsequence in heights of those sorted envelopes
        # for two envelopes that have the same width, one can not be fitted into another, we sort them in height reversely to make sure of that
        # for example, (5,7) and (5,10) should be like [... (5,10) ... (5,7) ...] after sorting
        # since (5,10) is before (5,7), and [... 10 ... 7 ... ] is not an increasing subsequence
        # we have guaranteed that envelopes with the same width won't fit into each other

        # how to sort?
        # in Python, built-in sorting is guaranteed to be stable
        # that is, the original order is preserved if two items have the same key
        # sort on the secondary attribute first, which is height in a reversed order
        envelopes.sort(key=lambda e: e[1], reverse=True)
        # then, sort on the primary attribute, which is width
        envelopes.sort(key=lambda e: e[0])
        # then, use DP to find the longest increasing subsequence, refer to #300

        # initialization, a single character is a increasing subsequence
        dp = [1] * len(envelopes)

        for i in range(0, len(envelopes)):
            for j in range(0, i):
                if envelopes[j][1] < envelopes[i][1]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp) if dp else 0  # input could be an empty list


print(Solution().maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3]]))

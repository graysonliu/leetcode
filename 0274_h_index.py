# Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.
#
# According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."
#
# Example:
#
# Input: citations = [3,0,6,1,5]
# Output: 3
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had
# received 3, 0, 6, 1, 5 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and the remaining
# two with no more than 3 citations each, her h-index is 3.
# Note: If there are several possible values for h, the maximum one is taken as the h-index.

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # my solution: O(nlogn)
        # h = 0
        # citations.sort(reverse=True)
        # for i in range(len(citations)):
        #     # we have i+1 elements having at least citations[i] citations each
        #     if i + 1 >= citations[i]:
        #         # we have at least citations[i] elements having at least citations[i] citations each
        #         # thus, h=citations[i]
        #         return max(h, citations[i])
        #         # we return the maximum between h and citations[i] directly since this will definitely be the maximum h
        #         # explanation: the candidate h is either citations[i] or i+1 in each iteration
        #         # for any iteration with i' following this iteration, since the list is sorted in descending order
        #         # the value of citations[i'] can be no more than citations[i]
        #         # if the candidate is i'+1, we must have i'+1<citations[i']<=citations[i], still less than citations[i]
        #         # thus, all possible h after this iteration are less than citations[i]
        #         # which is less than max(h, citations[i])
        #
        #     else:  # i+1<citations[i]
        #         # we have i+1 elements having at least i+1 citations each, since i+1<citations[i]
        #         h = max(h, i + 1)
        #
        # return h

        # bucket sort
        n = len(citations)
        buckets = [0] * (n + 1)  # n+1 buckets
        # if a paper is cited k times, buckets[k]++, if k is larger than n, buckets[n]++
        # logic behind it: the value of h cannot be larger than n, if a paper is cited more than n times, we change
        # it to being cited exact n times, this won't change the value of h
        for c in citations:
            if c > n:
                buckets[n] += 1
            else:
                buckets[c] += 1

        s = 0
        # from the end to the start
        for i in range(n, -1, -1):
            s += buckets[i]  # s is the number of papers that have at least i citations
            if s >= i:
                return i


print(Solution().hIndex([4, 4, 0, 0]))

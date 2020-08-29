# Given an array of citations sorted in ascending order (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.
#
# According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."
#
# Example:
#
# Input: citations = [0,1,3,5,6]
# Output: 3
# Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had
# received 0, 1, 3, 5, 6 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and the remaining
# two with no more than 3 citations each, her h-index is 3.
# Note:
#
# If there are several possible values for h, the maximum one is taken as the h-index.
#
# Follow up:
#
# This is a follow up problem to H-Index, where citations is now guaranteed to be sorted in ascending order.
# Could you solve it in logarithmic time complexity?
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # sorted list: binary search
        n = len(citations)
        left, right = 0, n - 1
        h = 0
        while left <= right:
            # we are trying to find the separator that separates h papers and N-h papers
            # those h papers are at the end of the list since the list is sorted

            mid = left + (right - left) // 2
            # mid separates the list into [0,mid-1] and [mid,n-1]
            # we have n-mid papers that have at least citations[mid] citations
            # a candidate h could be min(n-mid, citations[mid])

            if citations[mid] == n - mid:
                # this is a perfect separator
                # if we move mid towards the end (mid becomes larger),
                # the new n-mid will be no larger than the old n-mid
                # if we move mid towards the start (mid becomes smaller),
                # the new citations[mid] will be no larger than the old citations[mid]
                # candidate h = min(n-mid, citations[mid]),
                # thus, no matter how we move mid, the new h will be no larger than the old h
                return n - mid

            if citations[mid] > n - mid:
                # we have n-mid papers that have at least n-mid citations
                # candidate h=min(n-mid, citations[mid])=n-mid
                h = max(h, n - mid)
                # if we make n-mid larger, and citations[mid] smaller, h could be larger
                # thus, we move mid towards the start
                right = mid - 1
            else:  # citations[mid] < n - mid
                # we have at least citations[mid] papers that have at least citations[mid] citations
                # candidate h=min(n-mid, citations[mid])=citations[mid]
                h = max(h, citations[mid])
                # if we make n-mid smaller, and citations[mid] larger, h could be larger
                # thus, we move mid towards the end
                left = mid + 1
        return h

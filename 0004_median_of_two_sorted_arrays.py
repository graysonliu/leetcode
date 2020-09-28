# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#
# Follow up: The overall run time complexity should be O(log (m+n)).
#
#
#
# Example 1:
#
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:
#
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
# Example 3:
#
# Input: nums1 = [0,0], nums2 = [0,0]
# Output: 0.00000
# Example 4:
#
# Input: nums1 = [], nums2 = [1]
# Output: 1.00000
# Example 5:
#
# Input: nums1 = [2], nums2 = []
# Output: 2.00000
#
#
# Constraints:
#
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -10^6 <= nums1[i], nums2[i] <= 10^6
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # already sorted, and logarithm time complexity, we can easily think of binary search
        # ...... A[i-1] | A[i] ......
        # ...... B[j-1] | B[j] ......
        # we cut those two lists into two parts
        # to find the median, the number of elements of left parts should be equal to the right parts
        # or left parts only have one more element compared to the right parts if the total length is odd
        # also all numbers on the left should be no larger than numbers on the right
        # that is A[i-1]<=B[j], and B[j-1]<=A[i]
        # suppose len(A)=m, len(B)=n
        # we cut A on i, that is, the left part has i elements from A. 0<=i<=m
        # then we should cut B on j = (m+n+1)//2 - i, no matter m+n is odd or even
        # that will make the left have at most one more element compared to the right
        # since 0<=i<=m, to make sure that j is not a negative number, we should guarantee that m<=n
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        # use binary search to find the perfect cut
        left, right = 0, m
        while left <= right:
            i = left + (right - left) // 2
            j = (m + n + 1) // 2 - i
            # i+j=(m+n+1)//2, meaning that the left part will have at least one element
            # otherwise m+n=0, meaning both lists are empty, which is invalid input
            max_of_left = max(nums1[i - 1] if i > 0 else float('-inf'), nums2[j - 1] if j > 0 else float('-inf'))
            min_of_right = min(nums1[i] if i < m else float('inf'), nums2[j] if j < n else float('inf'))

            # perfect cut
            if max_of_left <= min_of_right:
                return max_of_left if (m + n) & 1 == 1 else (max_of_left + min_of_right) / 2

            # cut is not perfect
            if i != 0 and max_of_left == nums1[i - 1]:
                # meaning that A[i-1]>B[j], i is too large, we should decrease i
                right = i - 1
            elif j != 0 and max_of_left == nums2[j - 1]:
                # meaning that B[j-1]>A[i], j is too large, that is because i is too small, we should increase i
                left = i + 1

            # now consider edge cases, i=0 or j=0
            # i=0 and j=0 cannot happen at the same time, otherwise the left part will be empty
            if i == 0:
                # i=0 and the cut is still not perfect, increase i is the only option since i=0 is the smallest
                left = i + 1
            elif j == 0:
                # j=0 and the cut is still not perfect, increase j is the only option since j=0 is the smallest
                # that means we should decrease i
                right = i - 1

        # if we need to find the kth smallest number of these two sorted lists
        # we should make j=k-i


if __name__ == "__main__":
    print(Solution().findMedianSortedArrays([2], []))

# Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.
#
# Formally the function should:
#
# Return true if there exists i, j, k
# such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
# Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.
#
# Example 1:
#
# Input: [1,2,3,4,5]
# Output: true
# Example 2:
#
# Input: [5,4,3,2,1]
# Output: false

from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # related problem: #0300
        # the O(nlogn) solution from #0300 (see its 4th approach of leetcode official solution)
        # this solution is actually O(n) in this problem
        seq = []
        for num in nums:
            import bisect
            i = bisect.bisect_left(seq, num)  # since the length of seq will be at most 3, this is actually O(1)
            if i >= len(seq):
                seq.append(num)
                if len(seq) >= 3:  # since the length of seq will be at most 3, this solution uses O(1) space
                    return True
            else:
                seq[i] = num
        return False

# Given two arrays, write a function to compute their intersection.
#
# Example 1:
#
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:
#
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Note:
#
# Each element in the result should appear as many times as it shows in both arrays.
# The result can be in any order.
# Follow up:
#
# What if the given array is already sorted? How would you optimize your algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is better?
# What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        import collections
        counter1 = collections.Counter(nums1)
        counter2 = collections.Counter(nums2)
        if len(counter1) > len(counter2):
            counter1, counter2 = counter2, counter1
        for num in counter1:
            if num in counter2:
                counter1[num] = min(counter1[num], counter2[num])
            else:
                counter1[num] = 0
        return list(counter1.elements())

        # more concise version
        from collections import Counter
        return list((Counter(nums1) & Counter(nums2)).elements())

        # follow up: what if these two lists have been sorted
        nums1.sort()
        nums2.sort()
        # two pointers
        p1, p2 = 0, 0
        res = []
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                res.append(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
        return res

        pass

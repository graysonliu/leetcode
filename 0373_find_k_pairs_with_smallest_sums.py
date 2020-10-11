# You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.
#
# Define a pair (u,v) which consists of one element from the first array and one element from the second array.
#
# Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.
#
# Example 1:
#
# Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
# Output: [[1,2],[1,4],[1,6]]
# Explanation: The first 3 pairs are returned from the sequence:
# [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
# Example 2:
#
# Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
# Output: [1,1],[1,1]
# Explanation: The first 2 pairs are returned from the sequence:
# [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
# Example 3:
#
# Input: nums1 = [1,2], nums2 = [3], k = 3
# Output: [1,3],[2,3]
# Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        import itertools
        # solution1: brute force 1
        # note that the product elements of itertools.product() are tuples
        return list(map(list, sorted(itertools.product(nums1, nums2), key=sum)[:k]))

        # solution2: brute force 2 using heapq
        import heapq
        return heapq.nsmallest(k, ([u, v] for u in nums1 for v in nums2), key=sum)

        # solution3: similar to merge sort
        # we have m*n pairs, imagine a m*n matrix
        rows = map(lambda u: ([u, v] for v in nums2), nums1)
        # since both nums1 and nums2 are ascending
        # each row is already sorted based on the sum of u and v
        # regular slicing cannot be applied to generator since 'generator' object does not have __getitem__
        # we should use itertools.islice
        return list(itertools.islice(heapq.merge(*rows, key=sum), k))

        # solution4
        res = []
        m, n = len(nums1), len(nums2)
        if m == 0 or n == 0:
            return res
        # imagine a m*n matrix, M[0][0] is the smallest
        # the next pair should be either M[0][1] or M[1][0]
        # x ? . . .
        # ? . . . .
        # . . . . .
        # x represents a pair that has been added to res
        # ? represents a candidate for the next pair
        # if M[1][0] has a smaller sum, the matrix would be like this:
        # x x ? . .
        # ? . . . .
        # . . . . .
        # we add all candidates in a heap queue, which will always pop the smallest element
        # how to choose new candidates after we added one pair to res?
        # to the added pair, the pair on its right and the pair below it should be considered
        # but that is not always the case, the previous example, after we add M[0][1] to res
        # we only put M[0][2] into the heap as the new candidate
        # because the pair below M[0][1], which is M[1][1], is surely larger than M[1][0], which is already a candidate
        # so, for each row, it can have at most one candidate, and it should be the leftmost '?'
        # for each column, it can have at most one candidate, and it should be the topmost '?'
        # we have to maintain two list, one for row, and one for columns
        h = [(nums1[0] + nums2[0], 0, 0)]  # candidates
        have_candidate_rows = [True] + [False] * (m - 1)
        have_candidate_cols = [True] + [False] * (n - 1)

        heapq.heapify(h)
        while len(res) < k and len(h) != 0:  # exit loop if we have k pairs in res or there are no candidates left
            s, i, j = heapq.heappop(h)
            # the row and the column where the pair at lost their candidate
            have_candidate_rows[i] = False
            have_candidate_cols[j] = False

            res.append([nums1[i], nums2[j]])

            if j + 1 < n and not have_candidate_cols[j + 1]:  # the pair on its right
                heapq.heappush(h, (nums1[i] + nums2[j + 1], i, j + 1))
                have_candidate_rows[i] = True
                have_candidate_cols[j + 1] = True
            if i + 1 < m and not have_candidate_rows[i + 1]:  # the pair below it
                heapq.heappush(h, (nums1[i + 1] + nums2[j], i + 1, j))
                have_candidate_rows[i + 1] = True
                have_candidate_cols[j] = True
        return res


print(Solution().kSmallestPairs(nums1=[1, 7, 11], nums2=[2, 4, 6], k=3))

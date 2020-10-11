# Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.
#
# Note that it is the kth smallest element in the sorted order, not the kth distinct element.
#
# Example:
#
# matrix = [
#              [ 1,  5,  9],
#              [10, 11, 13],
#              [12, 13, 15]
#          ],
# k = 8,
#
# return 13.
# Note:
# You may assume k is always valid, 1 ≤ k ≤ n^2.

from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # we can treat it as a multi-way merge, similar to #0023
        # #0023 only requires each row to be sorted
        # in this problem, each column is also sorted, making it similar to solution4 of #0373
        # the smallest is definitely M[0][0], after we checked M[0][0], there are two new candidates to be considered in the next iteration
        # this would be the element on its right, and the element below it
        # x ? . . .
        # ? . . . .
        # . . . . .
        # since each row is sorted as well as each col, we only need one candidate in each row and each col
        # that would be the leftmost unchecked element in each row, and topmost unchecked element in each col
        # basically the same as solution4 of #0373, using heapq
        # or we can use heapq.merge() directly, but this is more similar to the solution in #0023 since it does not consider that columns are also sorted

        # solution1: using heapq.merge()
        import heapq
        g = heapq.merge(*matrix)  # this is a generator
        for _ in range(k):
            res = next(g)
        return res

        # solution2: same as solution4 in #0373
        import heapq
        h = [(matrix[0][0], 0, 0)]
        heapq.heapify(h)

        # for checked element, we try to add adjacent element on its right and below it to the heap
        # but if the row or the col that the new candidate at already has candidate in the heap, we should not add the new candidate
        # remember: leftmost for each row and topmost for each col
        m, n = len(matrix), len(matrix[0])
        have_candidate_rows = [True] + [False] * (n - 1)
        have_candidate_cols = [True] + [False] * (n - 1)

        for _ in range(k):
            v, i, j = heapq.heappop(h)
            have_candidate_rows[i] = False
            have_candidate_cols[j] = False

            if j + 1 < n and not have_candidate_cols[j + 1]:  # the pair on its right
                heapq.heappush(h, (matrix[i][j + 1], i, j + 1))
                have_candidate_rows[i] = True
                have_candidate_cols[j + 1] = True
            if i + 1 < m and not have_candidate_rows[i + 1]:  # the pair below it
                heapq.heappush(h, (matrix[i + 1][j], i + 1, j))
                have_candidate_rows[i + 1] = True
                have_candidate_cols[j] = True

        return v


print(Solution().kthSmallest([[1, 5, 9],
                              [10, 11, 13],
                              [12, 13, 15]], 8))

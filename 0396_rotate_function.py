# Given an array of integers A and let n to be its length.
#
# Assume Bk to be an array obtained by rotating the array A k positions clock-wise, we define a "rotation function" F on A as follow:
#
# F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1].
#
# Calculate the maximum value of F(0), F(1), ..., F(n-1).
#
# Note:
# n is guaranteed to be less than 10^5.
#
# Example:
#
# A = [4, 3, 2, 6]
#
# F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
# F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
# F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
# F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26
#
# So the maximum value of F(0), F(1), F(2), F(3) is F(3) = 26.

from typing import List


class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        # brutal force, O(n^2)
        # Time Limit Exceeded
        n = len(A)
        if n == 0:
            return 0
        res = float('-inf')
        for i in range(n):
            j = 0
            s = 0
            for j, num in enumerate(A):
                s += ((j + i) % n) * num
            res = max(res, s)
        return res

        # better solution, O(n)
        # F(0) = 0 * A[0] + 1 * A[1] + 2 * A[2] + ... + (n-1) * A[n-1]
        # F(1) = 0 * A[n-1] + 1 * A[0] + 2 * A[1] + ... + (n-1) * A[n-2]
        # F(1) - F(0) = A[0] + A[1] + A[2] + ... + A[n-1] - (n-1) * A[n-1]
        #             = sum(A) - n * A[n-1]
        # similarly, F(2) - F(1) = sum(A) - n * A[n-2]
        # F(k) - F(k-1) = sum(A) - n * A[n-k]
        # F(k) = F(k-1) + sum(A) - n * A[n-k], 1<=k<=n-1
        n = len(A)
        if n == 0:
            return 0
        s = sum(A)
        f = sum([i * num for i, num in enumerate(A)])  # calculate F(0)
        res = f
        for k in range(1, n):
            f = f + s - n * A[n - k]
            res = max(res, f)
        return res


print(Solution().maxRotateFunction([4, 3, 2, 6]))

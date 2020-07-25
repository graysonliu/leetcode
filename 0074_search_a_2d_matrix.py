# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# Example 1:
#
# Input:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 3
# Output: true
# Example 2:
#
# Input:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 13
# Output: false

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        # binary search
        # first, confirm the row number
        top, bottom = 0, len(matrix) - 1
        while top <= bottom:
            mid = top + (bottom - top) // 2
            if target == matrix[mid][0]:
                return True
            elif target < matrix[mid][0]:
                if mid == 0:
                    return False
                elif target >= matrix[mid - 1][0]:
                    row = mid - 1
                    break
                else:
                    bottom = mid - 1
            elif target > matrix[mid][0]:
                if mid == len(matrix) - 1 or target < matrix[mid + 1][0]:
                    row = mid
                    break
                else:
                    top = mid + 1

        # search confirmed row
        left, right = 0, len(matrix[0]) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if target == matrix[row][mid]:
                return True
            elif target < matrix[row][mid]:
                right = mid - 1
            elif target > matrix[row][mid]:
                left = mid + 1
        return False

    # easier solution: left, right = 0, m*n-1
    # mid = (left+right)//2
    # to confirm the location of mid: matrix[mid//n][mid%n]


print(Solution().searchMatrix([[1, 3, 5, 7],
                               [10, 11, 16, 20],
                               [23, 30, 34, 50]
                               ], 23))

# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
# Example:
#
# Consider the following matrix:
#
# [
#     [1,   4,  7, 11, 15],
#     [2,   5,  8, 12, 19],
#     [3,   6,  9, 16, 22],
#     [10, 13, 14, 17, 24],
#     [18, 21, 23, 26, 30]
# ]
# Given target = 5, return true.
#
# Given target = 20, return false.

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # if the search target exists in the matrix
        # it should between the top-left number and the bottom-right number
        # principle 1: it is either in the range of the top row or the right column
        # principle 2: it is either in the range of the left column or the bottom row
        # thus, we eliminate one row and one column per iteration, like peeling an onion
        # however, we can choose to use only one of these two principles to simplify the code
        # that is, we eliminate one row or one column each iteration
        # the time complexity is O(m+n), where m is the number of rows and n is the number of columns
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        # we use the second principle, so we start from the bottom-left corner
        row, col = len(matrix) - 1, 0
        n = len(matrix[0]) - 1  # the rightest column
        while True:
            if target < matrix[0][col] or target > matrix[row][n]:
                return False
            if target == matrix[row][col]:
                return True
            if matrix[0][col] <= target < matrix[row][col]:
                # eliminate the bottom row
                row -= 1
            else:  # eliminate the left column
                col += 1


print(Solution().searchMatrix([[1, 4, 7, 11, 15],
                               [2, 5, 8, 12, 19],
                               [3, 6, 9, 16, 22],
                               [10, 13, 14, 17, 24],
                               [18, 21, 23, 26, 30]], 5))

# Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
#
# Range Sum Query 2D
# The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.
#
# Example:
# Given matrix = [
#     [3, 0, 1, 4, 2],
#     [5, 6, 3, 2, 1],
#     [1, 2, 0, 1, 5],
#     [4, 1, 0, 1, 7],
#     [1, 0, 3, 0, 5]
# ]
#
# sumRegion(2, 1, 4, 3) -> 8
# sumRegion(1, 1, 2, 2) -> 11
# sumRegion(1, 2, 2, 4) -> 12
# Note:
# You may assume that the matrix does not change.
# There are many calls to sumRegion function.
# You may assume that row1 ≤ row2 and col1 ≤ col2.
from typing import List


class NumMatrix:
    # # my solution: similar to 0303, we calculate sums per row
    # def __init__(self, matrix: List[List[int]]):
    #     rows = len(matrix)
    #     if rows == 0:
    #         return
    #     cols = len(matrix[0])
    #
    #     sums = []
    #     for r in range(rows):
    #         sums.append([0] * (cols + 1))
    #         for c in range(1, cols + 1):
    #             sums[r][c] = sums[r][c - 1] + matrix[r][c - 1]
    #     self.sums = sums
    #
    # def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
    #     s = 0
    #     for r in range(row1, row2 + 1):
    #         s += (self.sums[r][col2 + 1] - self.sums[r][col1])
    #     return s

    # a smarter solution: calculate sums for every rectangle whose left-top element is [0][0] (point O)
    # O
    #   .
    #    .
    #     A ... B
    #     .     .
    #     .     .
    #     C ... D
    # then, S(ABCD)=S(OD)-S(OB)-S(OC)+S(OA)
    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        if rows == 0:
            return
        cols = len(matrix[0])

        sums = [[0] * (cols + 1) for _ in range(rows + 1)]  # using generator to initialize 2D list
        # don't use [[0] * (cols + 1)] * (rows + 1), since every row is a reference to the same list
        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                sums[r][c] = sums[r - 1][c] + sums[r][c - 1] - sums[r - 1][c - 1] + matrix[r - 1][c - 1]
        self.sums = sums

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sums[row2 + 1][col2 + 1] - self.sums[row1][col2 + 1] - self.sums[row2 + 1][col1] + self.sums[row1][col1]
    # compared to the previous approach, they both have O(rows*cols) space complexity
    # the first one has O(rows) time complexity when calling sumRegion()
    # however, the second one has O(1) time complexity when calling sumRegion()


m = NumMatrix([[3, 0, 1, 4, 2],
               [5, 6, 3, 2, 1],
               [1, 2, 0, 1, 5],
               [4, 1, 0, 1, 7],
               [1, 0, 3, 0, 5]])
print(m.sumRegion(2, 1, 4, 3))

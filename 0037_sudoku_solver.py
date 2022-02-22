# Write a program to solve a Sudoku puzzle by filling the empty cells.

# A sudoku solution must satisfy all of the following rules:

# 1. Each of the digits 1-9 must occur exactly once in each row.
# 2. Each of the digits 1-9 must occur exactly once in each column.
# 3. Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.

# Example 1:

# Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
# Explanation: The input board is shown above and the only valid solution is shown below:

# Constraints:

# board.length == 9
# board[i].length == 9
# board[i][j] is a digit or '.'.
# It is guaranteed that the input board has only one solution.

from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows_available_set = [[True for i in range(9)] for i in range(9)]
        cols_available_set = [[True for i in range(9)] for i in range(9)]
        sub_boxes_available_set = [[True for i in range(9)] for i in range(9)]
        vacant_list = []

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    index = num - 1
                    rows_available_set[i][index] = False
                    cols_available_set[j][index] = False
                    sub_boxes_available_set[i // 3 * 3 + j // 3][index] = False
                else:
                    vacant_list.append((i, j))

        def backtrack(vacant_list, cur):
            if len(vacant_list) == cur:
                return True
            i, j = vacant_list[cur]
            for num in range(1, 10):
                index = num - 1
                if rows_available_set[i][index] and cols_available_set[j][index] and sub_boxes_available_set[i // 3 * 3 + j // 3][index]:
                    board[i][j] = str(num)
                    rows_available_set[i][index] = False
                    cols_available_set[j][index] = False
                    sub_boxes_available_set[i // 3 * 3 + j // 3][index] = False
                    res = backtrack(vacant_list, cur + 1)
                    if res:
                        return True
                    else:
                        board[i][j] = '.'
                        rows_available_set[i][index] = True
                        cols_available_set[j][index] = True
                        sub_boxes_available_set[i //
                                                3 * 3 + j // 3][index] = True
            return False

        backtrack(vacant_list, 0)


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
                                                                                                                                                                                                      ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
Solution().solveSudoku(board)
print(board)

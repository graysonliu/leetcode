# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
#
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
#
# Example:
#
# X X X X
# X O O X
# X X O X
# X O X X
# After running your function, the board should be:
#
# X X X X
# X X X X
# X X X X
# X O X X
# Explanation:
#
# Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # find every O-region touches border, change all these regions from 'O' to 'S'
        # change all non 'S' to 'X', and all 'S' to 'O'

        if not any(board):
            return

        m, n = len(board), len(board[0])
        border_adjacent = []
        for i in range(0, n):
            border_adjacent += [(0, i), (m - 1, i)]
        for i in range(0, m):
            border_adjacent += [(i, 0), (i, n - 1)]

        while any(border_adjacent):
            (i, j) = border_adjacent.pop()
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = 'S'
                border_adjacent += [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]

        for i in range(m):
            for j in range(n):
                board[i][j] = 'O' if board[i][j] == 'S' else 'X'


board = [['X', 'X', 'X', 'X'],
         ['X', 'O', 'O', 'X'],
         ['X', 'X', 'O', 'X'],
         ['X', 'O', 'X', 'X']]
Solution().solve(board)
print(board)

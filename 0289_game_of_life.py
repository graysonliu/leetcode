# According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
#
# Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):
#
# Any live cell with fewer than two live neighbors dies, as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.
#
# Example:
#
# Input:
# [
#     [0,1,0],
#     [0,0,1],
#     [1,1,1],
#     [0,0,0]
# ]
# Output:
# [
#     [0,0,0],
#     [1,0,1],
#     [0,1,1],
#     [0,1,0]
# ]
# Follow up:
#
# Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
# In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?

from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows = len(board)
        if rows == 0:
            return
        cols = len(board[0])

        # # my solution: O(rows*cols) space complexity
        # def get_sum(r1, r2, c1, c2):
        #     if r1 < 0:
        #         return get_sum(0, r2, c1, c2)
        #     if r2 > rows:
        #         return get_sum(r1, rows, c1, c2)
        #     if c1 < 0:
        #         return get_sum(r1, r2, 0, c2)
        #     if c2 > cols:
        #         return get_sum(r1, r2, c1, cols)
        #     s = 0
        #     for r in range(r1, r2):
        #         s += sum(board[r][c1:c2])
        #     return s
        #
        # temp = {}
        #
        # for i in range(rows):
        #     for j in range(cols):
        #         neighbors = get_sum(i - 1, i + 2, j - 1, j + 2) - board[i][j]
        #         if (neighbors < 2 or neighbors > 3) and board[i][j] == 1:
        #             temp[(i, j)] = 0
        #         if neighbors == 3 and board[i][j] == 0:
        #             temp[(i, j)] = 1
        #
        # for t, v in temp.items():
        #     board[t[0]][t[1]] = v

        # # the O(1) space complexity solution
        # # when a update happens, if it is dead->live (0->1), we change the value to 2 rather than 1
        # # thus, we know this cell is originally 2
        # # similarly, for live->dead (1->0), we change the value to -1 rather than 0, indicating it is originally 1
        # # finally, we use another pass, changing all 2 to 1, and all -1 to 0
        # def get_sum(r1, r2, c1, c2):
        #     r1 = max(r1, 0)
        #     r2 = min(r2, rows)
        #     c1 = max(c1, 0)
        #     c2 = min(c2, cols)
        #     s = 0
        #     for r in range(r1, r2):
        #         for c in range(c1, c2):
        #             if abs(board[r][c]) == 1:  # the cell could be -1, which indicates its original value is 1
        #                 s += 1
        #     return s
        #
        # for i in range(rows):
        #     for j in range(cols):
        #         neighbors = get_sum(i - 1, i + 2, j - 1, j + 2) - board[i][j]
        #         if (neighbors < 2 or neighbors > 3) and board[i][j] == 1:
        #             board[i][j] = -1
        #         if neighbors == 3 and board[i][j] == 0:
        #             board[i][j] = 2
        #
        # for i in range(rows):
        #     for j in range(cols):
        #         if board[i][j] == 2:
        #             board[i][j] = 1
        #         elif board[i][j] == -1:
        #             board[i][j] = 0

        # follow up: if the board is extremely sparse, it would be better if we only focus those live cells
        # the idea is, for example:
        # 0 0 0 0 0
        # 1 0 1 0 0
        # 0 0 0 0 0
        # board[1][0] is a live cell, we add all its 8 neighbors to a list
        # board[1][2] is another live cell, we also add its 8 neighbors to the list
        # for [1][1], this element appears in the list twice, and its live neighbor count is exactly 2
        # this is also the case for all other cells, if a cell isn't in the list, its live neighbor count is just 0

        # so, we first find all live cells
        live = [(i, j) for i in range(rows) for j in range(cols) if board[i][j] == 1]
        # get the list of all cells that have at least one live cell as its neighbor
        # then, we count each one's appearance
        import collections
        count = collections.Counter((n_i, n_j)
                                    for i, j in live
                                    for n_i in range(i - 1, i + 2)
                                    for n_j in range(j - 1, j + 2)
                                    if not (n_i == i and n_j == j))
        # we will have out of range cells like [-1][0] in the count, but we will ignore these cells later
        # after the update, the new live cells should satisfy conditions as follows
        new_live = {ij for ij in count
                    if count[ij] == 3 or (count[ij] == 2 and ij in live)}  # this is a set, ij is a tuple
        # iterate the board, only cells in new_live should be assigned 1, all other cells are 0
        # all out of range cells are obviously ignored in the iteration
        for i in range(rows):
            for j in range(cols):
                board[i][j] = int((i, j) in new_live)


Solution().gameOfLife([[0, 1, 0],
                       [0, 0, 1],
                       [1, 1, 1],
                       [0, 0, 0]])

# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
#
# Example:
#
# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
#
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.
#
# Constraints:
#
# board and word consists only of lowercase and uppercase English letters.
# 1 <= board.length <= 200
# 1 <= board[i].length <= 200
# 1 <= word.length <= 10^3
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        try:
            n = len(board[0])
        except IndexError:
            return False

        # backtrack
        def backtrack(i, j, word, visited):
            if len(word) == 0:
                return True
            if i - 1 >= 0 and not (i - 1, j) in visited and board[i - 1][j] == word[0]:
                if backtrack(i - 1, j, word[1:], visited.union({(i - 1, j)})):
                    return True
            if i + 1 < m and not (i + 1, j) in visited and board[i + 1][j] == word[0]:
                if backtrack(i + 1, j, word[1:], visited.union({(i + 1, j)})):
                    return True
            if j - 1 >= 0 and not (i, j - 1) in visited and board[i][j - 1] == word[0]:
                if backtrack(i, j - 1, word[1:], visited.union({(i, j - 1)})):
                    return True
            if j + 1 < n and not (i, j + 1) in visited and board[i][j + 1] == word[0]:
                if backtrack(i, j + 1, word[1:], visited.union({(i, j + 1)})):
                    return True
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and backtrack(i, j, word[1:], {(i, j)}):
                    return True

        return False


print(Solution().exist(board=[['A', 'B', 'C', 'E'],
                              ['S', 'F', 'C', 'S'],
                              ['A', 'D', 'E', 'E']],
                       word="ABCB"))

# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:
#
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list.
# Note:
#
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
# Example 1:
#
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# Output: 5
#
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
# Example 2:
#
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# Output: 0
#
# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # bfs
        words = set(wordList)
        import queue
        Q = queue.Queue()
        Q.put((beginWord, 1))
        if beginWord in words:
            words.remove(beginWord)
        alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        length = len(beginWord)
        while not Q.empty():
            word, step = Q.get()
            if word == endWord:
                return step
            for i in range(length):
                for c in alphabet:
                    new_word = word[0:i] + c + word[i + 1:length]
                    if new_word in words:
                        Q.put((new_word, step + 1))
                        words.remove(new_word)
        return 0

        # solution 2: still bfs, but with bi-direction
        words = set(wordList)
        if endWord not in words:
            return 0
        s_begin = {beginWord}
        s_end = {endWord}
        s = {True: s_begin, False: s_end}
        visited_begin = {beginWord: 1}
        visited_end = {endWord: 1}
        visited = {True: visited_begin, False: visited_end}
        alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        length = len(beginWord)
        while len(s_begin) > 0 and len(s_end) > 0:
            begin_or_not = True if len(s_begin) <= len(s_end) else False  # always choose the smaller set to expand
            successors = set()
            for word in s[begin_or_not]:
                if word in visited[not begin_or_not]:
                    return visited_begin[word] + visited_end[word] - 1
                for i in range(length):
                    for c in alphabet:
                        new_word = word[0:i] + c + word[i + 1:length]
                        if new_word in words and new_word not in visited[begin_or_not]:
                            successors.add(new_word)
                            visited[begin_or_not][new_word] = visited[begin_or_not][word] + 1
            s[begin_or_not] = successors  # note: this changes the address of s[begin_or_not]
            # therefore, s[begin_or_not] does not point to the original s_begin (or s_end when begin_or_not is False)
            s_begin, s_end = s[True], s[False]  # we update them with new address
        return 0


print(Solution().ladderLength('hit', 'cog', ["hot", "dot", "dog", "lot", "log"]))

# Given a pattern and a string str, find if str follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.
#
# Example 1:
#
# Input: pattern = "abba", str = "dog cat cat dog"
# Output: true
# Example 2:
#
# Input:pattern = "abba", str = "dog cat cat fish"
# Output: false
# Example 3:
#
# Input: pattern = "aaaa", str = "dog cat cat dog"
# Output: false
# Example 4:
#
# Input: pattern = "abba", str = "dog dog dog dog"
# Output: false
# Notes:
# You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        # # bijection, similar to #0205
        # words = str.split()
        # return len(pattern) == len(words) and len(set(zip(pattern, words))) == len(set(pattern)) == len(set(words))

        # # another tricky solution
        # words = str.split()
        # # imagine map as an iteration
        # # for every iteration, we find the its first occurrence in the iterable
        # return list(map(pattern.index, pattern)) == list(map(words.index, words))

        # since index() is O(n), which is time-consuming, we can use a dict to record element's first occurrence
        occur = {}
        words = str.split()
        if len(pattern) != len(words):
            return False
        for i in range(len(pattern)):
            # since a single letter could also appears as a word in the word list
            # we use uppercase letter, which can be distinguished from the words since they are all lowercase
            letter = pattern[i].upper()
            word = words[i]
            if letter not in occur:
                occur[letter] = i
            if word not in occur:
                occur[word] = i
            if occur[letter] != occur[word]:
                return False
        return True

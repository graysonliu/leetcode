# Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.
#
# Example 1:
#
# Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
# Output: 16
# Explanation: The two words can be "abcw", "xtfn".
# Example 2:
#
# Input: ["a","ab","abc","d","cd","bcd","abcd"]
# Output: 4
# Explanation: The two words can be "ab", "cd".
# Example 3:
#
# Input: ["a","aa","aaa","aaaa"]
# Output: 0
# Explanation: No such pair of words.
#
#
# Constraints:
#
# 0 <= words.length <= 10^3
# 0 <= words[i].length <= 10^3
# words[i] consists only of lowercase English letters.

from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        res = 0
        w = [set(word) for word in words]
        for i in range(len(w)):
            for j in range(i + 1, len(w)):
                if w[i].isdisjoint(w[j]) and len(words[i]) * len(words[j]) > res:
                    res = len(words[i]) * len(words[j])
        return res

        # a better solution
        # we use 26 bits (a mask) to represent whether a letter is in a word
        # for example, 'aayz' -> 110....01, the first two bits represent 'z' and 'y', the last bit represents 'a'
        # if mask1 & mask2 == 0, then word1 and word2 don't share any same letter
        masks = [0] * len(words)
        for i, word in enumerate(words):
            for letter in word:
                masks[i] = masks[i] | (1 << (ord(letter) - ord('a')))
        res = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if masks[i] & masks[j] == 0 and len(words[i]) * len(words[j]) > res:
                    res = len(words[i]) * len(words[j])
        return res


print(Solution().maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))

# You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.
#
# You can return the answer in any order.
#
#
#
# Example 1:
#
# Input: s = "barfoothefoobarman", words = ["foo","bar"]
# Output: [0,9]
# Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
# The output order does not matter, returning [9,0] is fine too.
# Example 2:
#
# Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
# Output: []
# Example 3:
#
# Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
# Output: [6,9,12]
#
#
# Constraints:
#
# 1 <= s.length <= 10^4
# s consists of lower-case English letters.
# 1 <= words.length <= 5000
# 1 <= words[i].length <= 30
# words[i] consists of lower-case English letters.
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        if len(s) == 0 or len(words) == 0:
            return res
        word_len = len(words[0])
        total_len = word_len * len(words)
        from collections import Counter
        count = Counter(words)  # construct a word->count mapping

        for start in range(len(s) - total_len + 1):
            count_copy = count.copy()
            # check s[start : start + word_len * len(words)]
            for i in range(start, start + total_len, word_len):
                word = s[i:i + word_len]
                if word in count_copy:  # subtract matched word from count_copy
                    count_copy[word] -= 1
                    if count_copy[word] == 0:
                        count_copy.pop(word)
                else:
                    break
            if len(count_copy) == 0:  # meaning all words are matched
                res.append(start)
        return res


print(Solution().findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "good"]))

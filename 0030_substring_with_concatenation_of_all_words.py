# You are given a string, s, and a list of words, words, that are all of the same length.
# Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.
#
# Example 1:
#
# Input:
#   s = "barfoothefoobarman",
#   words = ["foo","bar"]
# Output: [0,9]
# Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
# The output order does not matter, returning [9,0] is fine too.
# Example 2:
#
# Input:
#   s = "wordgoodstudentgoodword",
#   words = ["word","student"]
# Output: []


class Solution:
    def findSubstring_1(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        # 这题有点问题，题目里面说words中的所有单词长度相同，但example 2不满足这一条件
        # 按照单词长度相同来做
        from collections import Counter
        if not s or not words:  # 空字符串或空列表
            return []

        res = []

        word_len = len(words[0])
        words_count = len(words)
        window_len = word_len * words_count  # 滑动窗口大小，即匹配的字符串长度
        c = Counter(words)  # Counter是dict的一个子类，用于计数

        for i in range(0, len(s) - window_len + 1):
            window_words = [s[j:j + word_len] for j in range(i, i + window_len, word_len)]  # 将窗口分词
            if Counter(window_words) == c:
                res.append(i)

        return res

    def findSubstring(self, s, words):
        # 方法改进
        from collections import Counter

        if not s or not words:
            return []

        res = []

        word_len = len(words[0])
        words_count = len(words)
        window_len = word_len * words_count
        count = Counter(words)

        for i in range(word_len):  # 所有词的长度相同，所以对整个字符串s来说，只有word_len种分词的方式
            start_index = cuur_index = i
            curr_count = dict()
            while cuur_index + word_len <= len(s):
                cuur_word = s[cuur_index:cuur_index + word_len]
                cuur_index += word_len
                if cuur_word not in words:  # 有一个词不对，把开始位置start_index设为当前位置curr_index，重新开始
                    curr_count.clear()
                    start_index = cuur_index
                else:
                    curr_count[cuur_word] = curr_count.get(cuur_word, 0) + 1
                    while curr_count[cuur_word] > count[cuur_word]:  # 当前的词多了，start_index后移
                        start_word = s[start_index:start_index + word_len]
                        start_index += word_len
                        curr_count[start_word] -= 1
                    if cuur_index - start_index == window_len:
                        res.append(start_index)

        return res


if __name__ == "__main__":
    print(Solution().findSubstring("wordgoodstudentgoodword", ["word", "student"]))

# coding=utf-8
# Given a string, find the length of the longest substring without repeating characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a
# subsequence and not a substring.

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        核心思想是逐个找到以每个字符为起点的最长无重复子串，简单的brute force
        '''
        # 使用集合set
        lookup_set = set()

        total_len = len(s)
        max_len = 0

        # range用法
        # range(stop)
        # range(start, stop[, step])
        for i in range(total_len):
            lookup_set.clear()
            for j in range(i, total_len):
                # 查找key，时间复杂度O(1)
                if not s[j] in lookup_set:
                    lookup_set.add(s[j])
                else:
                    break
            max_len = max(max_len, len(lookup_set))

        return max_len

    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        更好的做法是用滑动窗口的思想
        假设程序当前维护的无重复子串为abcdefg，我们读取的下一个字符为子串最后一个字符g后面紧跟着的一个字符，假设其为d
        当我们读取到这个d时，由于字符d在当前子串中出现过，我们需要把窗口的左边沿移动到出现过的字符d的后面，即维护的子串变为efgd
        利用这种思想，我们只需要记录每个出现过字符的最大索引
        '''
        max_indices = dict()
        start, max_len = 0, 0
        for i, char in enumerate(s):
            if char in max_indices:
                start = max(start, max_indices[char] + 1)
            max_len = max(max_len, i - start + 1)
            max_indices[char] = i
        return max_len


'''
若字符均为ASCII中的字符，可以建立一个长度为256的list记录每个ASCII字符出现过的最大位置
注意指定长度list的初始化，[0 for _ in range(256)]
ord()用于字符转ASCII码，chr()用于ASCII码转字符
'''

if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring2("abcabcbb"))

# Implement strStr().
#
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
# Example 1:
#
# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:
#
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# Clarification:
#
# What should we return when needle is an empty string? This is a great question to ask during an interview.
#
# For the purpose of this problem, we will return 0 when needle is an empty string.
# This is consistent to C's strstr() and Java's indexOf().

class Solution:
    def strStr(self, haystack, needle):
        return haystack.find(needle)

    def strStr1(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1

    def strStr2(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        # 递归的方法很蠢，交上去内存溢出
        def match_first_char(str1, str2):
            return str1 and str1[0] == str2[0]

        def match_str(str1, str2):
            if not str2:
                return True
            return match_first_char(str1, str2) and match_str(str1[1:], str2[1:])

        if not needle:
            return 0

        for i in range(len(haystack)):
            if match_str(haystack[i:], needle):
                return i

        return -1


if __name__ == '__main__':
    print(Solution().strStr("hello", "as"))

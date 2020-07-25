# Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
#
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).
#
# Note:
#
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like . or *.
# Example 1:
#
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:
#
# Input:
# s = "aa"
# p = "a*"
# Output: true
# Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
# Example 3:
#
# Input:
# s = "ab"
# p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
# Example 4:
#
# Input:
# s = "aab"
# p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".
# Example 5:
#
# Input:
# s = "mississippi"
# p = "mis*is*p*."
# Output: false

class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        """
        感觉有点难，直觉是用递归，但没有具体思路
        看了solution，递归的做法依然是一个一个字符的比较
        核心是对*的处理
        """
        # 先考虑输入为空字符串的情况，字符串s和模板p均可能为空
        # 当s为空时，若p不为空，二者仍然可能匹配，例如s='', p='a*'
        # 不过，如果p为空，则只有当s为空时二者才可能匹配
        # 直接用字符串的真值判定是否为空
        if not p:  # 若p为空
            return not s  # 只有s也为空时才可能匹配

        # 又是trick，用bool()避免写if语句，bool(s)用来确保s不为空，否则后面会越界
        first_match = bool(s) and p[0] in {s[0], '.'}
        # 这里的first_match是在不考虑*的情况下判断s和p开头的第一个字符是否匹配

        # 考虑*的情况
        if len(p) >= 2 and p[1] == '*':
            # 第一种情况，*之前的字符出现0次，那么砍掉p的*，即用s和p[2:]做匹配
            # 第二种情况，假设*之前的字符在s中出现过，那么接下来匹配s[1:]和p，s一直被砍头直到变为第一种情况
            return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))
        # 没有*出现，s和p均被砍头继续比较
        else:
            return first_match and self.isMatch(s[1:], p[1:])

    # 用动态规划保存中间结果
    def isMatch1(self, s, p):
        # cache[i,j]用于保存s[i:]与p[j:]的匹配结果
        # 实际上cache[i,j]是cache[(i,j)]，字典某个item的key为tuple时圆括号被省略掉了
        # python基础：dict的key只能是不可变的，故tuple可以做key，而list不能作为key
        cache = dict()

        def dp(i, j):
            if (i, j) in cache:
                return cache[i, j]
            # p[j:]为空， s[i:]也为空时才能匹配
            if len(p) <= j:
                cache[i, j] = i >= len(s)
                return cache[i, j]
            # 后面其实还是递归，但保存了所有的中间结果，避免了同一个cache[i,j]的重复计算，也避免了字符串切片操作
            first_match = i < len(s) and p[j] in {s[i], '.'}
            if len(p[j:]) >= 2 and p[j:][1] == '*':
                cache[i, j] = dp(i, j + 2) or (first_match and dp(i + 1, j))
            else:
                cache[i, j] = first_match and dp(i + 1, j + 1)
            return cache[i, j]

        return dp(0, 0)


if __name__ == '__main__':
    print(Solution().isMatch('ab', '.*c'))

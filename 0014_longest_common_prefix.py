# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:
#
# All given inputs are in lowercase letters a-z.


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        # 把第一个字符串拿出来，后面所有的字符串跟第一个比较
        s_f = strs[0]
        while len(s_f) > 0:
            match_flag = True
            for s in strs[1:]:
                if s.find(s_f) != 0:
                    match_flag = False
                    break
            if match_flag:
                return s_f
            else:
                # 每匹配失败一次，s_f就砍一个尾巴
                s_f = s_f[:-1]
        # s_f变为空会跳出循环，说明没有共同的前缀，返回空字符串
        return ''

    def longestCommonPrefix1(self, strs):
        if not strs:
            return ''
        # zip()的用法！！！zip(*)为zip()的逆运算
        for i, ch in enumerate(zip(*strs)):
            # 这里的set()将zip()输出的tuple转为集合，即消除重复元素
            if len(set(ch)) != 1:
                return strs[0][:i]
        # 注意zip只会返回公有长度的部分，例如zip(*["fl","fls"])的结果为[('f', 'f'), ('l', 'l')]
        # 这种情况下循环里的返回语句不会执行，即公有前缀的结果就是strs中最短的字符串
        # min函数关键字key的用法，key指定一个函数，len为求字符串长度的函数，即下面语句的意思就是返回strs中最短的字符串
        return min(strs, key=len)


if __name__ == '__main__':
    print(Solution().longestCommonPrefix1(["fl", "fls"]))

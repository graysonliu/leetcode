# coding=utf-8
# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#
# Example 1:
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:
#
# Input: "cbbd"
# Output: "bb"


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 找最长回文子串
        # 中心扩展的思想，时间复杂度O(N^2)
        s_len = len(s)
        sub_str = ''  # 保存最长回文子串
        for i in range(s_len):
            left = right = i
            # 向后找到连续的与中心字符相同的字符，扩展右边界，这样就不用讨论回文子串奇偶性的问题
            while right + 1 < s_len and s[right + 1] == s[i]:
                right = right + 1
            while left - 1 >= 0 and right + 1 < s_len and s[left - 1] == s[right + 1]:
                left, right = left - 1, right + 1
            if right - left + 1 > len(sub_str):
                sub_str = s[left:right + 1]
        return sub_str

    # Manacher算法
    def longestPalindrome2(self, s):
        """
        算法思想是利用已找到回文子串的对称性
        举个例子，例如对于字符串dabaacaabaee，我们依然从第一个字符开始往后遍历
        遍历到第三个字符b时，依然用中心扩展，找到以该字符为中心的最长回文子串aba
        当遍历到第六个字符c时，能够找到以该字符为中心的最长回文子串abaacaabaa
        继续向后遍历，当遍历到倒数第四个字符b时，同样找到以该字符为中心的最长回文子串aba
        这时候我们发现，以第三个字符b与倒数第四个字符b为中心时得到的结果相同
        深入思考，这是必然的，因为以它们为中心字符找到的最长回文子串，都属于以c为中心得到的最长回文子串abaacaaba的一部分
        那么，在遍历到倒数第四个字符b时，由回文子串内的对称性，我们可以使用之前遍历到第三个字符b时的结果
        也就是说，如果我们遍历到的某个字符在我们之前得到的某个回文子串中，那么就可以利用该回文子串内的对称性避免一些重复的计算
        实际上Manacher算法还是中心扩展，只不过是利用了回文子串内对称的特性
        """
        """
        我们用一个数组P来记录以每个字符为中心能够扩展的最远距离
        例如上面的例子中，第三个字符b对应P[2]=1，第六个字符c对应P[5]=4，倒数第四个字符b对应P[8]=1
        另外定义“最远回文子串”，其含义为已经找到的右边界最靠右的回文子串，该子串不一定为最长回文子串
        需要“最远回文子串”的原因是，我们在从左至右遍历的过程中，希望已找到的回文子串其对称性使用范围能够向后延伸的最远
        还需要注意的是，对称性仅在回文子串*内*成立，不能超过其右边界
        索引：0 1 2 ... l ... i' ... c ... i ... r ... m
        假设P[i']和P[i]对应的字符关于最远回文子串的中心字符对称，其中心字符的索引为c，左右边界字符的索引分别为l和r，那么
        if P[i']<r-i:  # 确保在回文子串内利用对称性
            P[i]=P[i']
        else
            p[i]=r-i
        然后以P[i]为基础，继续向两边扩展，直到得到最终的P[i]
        """

        # 首先插入字符'#'以解奇偶性讨论的问题，因为需要使用对称性，所以之前找连续相同字符的办法不适用
        s = self.pre_process(s)

        f_r = 1  # 记录最远回文子串的右边界
        f_c = 1  # 记录最远回文子串的中心字符
        max_c = 1  # 记录最长回文子串的中心字符

        P = [0] * len(s)  # 更好的指定长度list初始化方法
        for i in range(1, len(s) - 1):  # 两个用于标记边界的字符不加入循环
            if i < f_r:  # 当前字符位于最远右边界内
                P[i] = min(P[2 * f_c - i], f_r - i)  # P[2*f_c-i]即为P[i']
            # 继续向两边扩展
            while s[i - P[i] - 1] == s[i + P[i] + 1]:
                P[i] += 1
            # 更新最远回文子串
            if i + P[i] > f_r:
                f_r = i + P[i]
                f_c = i
            # 更新最长回文子串
            if P[i] > P[max_c]:
                max_c = i
        return s[max_c - P[max_c]:max_c + P[max_c] + 1].replace('#', '')

    """
    关于Manacher算法的时间复杂度为什么是O(N)，代码中有两层循环，看起来貌似是O(N^2)
    仔细观察内层循环，我们会发现，内层循环每执行一次，最远回文子串的右边界f_r都会加一
    实际上，如果P[i']<f_r-i，内层while循环不会执行，因为此时是必然无法继续向两边扩展的，否则由对称性，P[i']应该更大才对
    而如果P[i']>f_r-i，则内层while循环会执行，P[i]的初始取值为f_r-i或0(i>=f_r时)，继续扩展会超出当前的最远右边界
    也就是说，内层while循环执行的总次数次数应该为f_r增加的值，而f_r初始值为1，最大也不可能超过字符串的长度，故内层循环执行次数为O(N)
    考虑到字符串经过填充长度增加，时间复杂度应该为O(2N)~O(N)
    """

    def pre_process(self, s):
        """
        例如，输入aba，处理后变为^#a#b#a#$
        这里的trick是，在开头加上一个^字符，结尾加上一个$字符，因为这两个字符不可能重复，中心扩展最多到此处停止，所以扩展过程中不需要再检查边界
        """
        new_s = '^'
        for char in s:
            new_s += ('#' + char)
        new_s += '#$'
        return new_s


if __name__ == "__main__":
    print(Solution().longestPalindrome('cbbd'))

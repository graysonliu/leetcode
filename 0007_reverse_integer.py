# coding=utf-8
# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
# Input: 123
# Output: 321
# Example 2:
#
# Input: -123
# Output: -321
# Example 3:
#
# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1].
# For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0

        s, s_reverse = str(x), str()
        # 逆序构建新字符串
        for c in range(len(s) - 1, -1, -1):
            s_reverse += s[c]
        # 逆序后第一个数字为0则舍弃
        if s_reverse[0] == '0':
            s_reverse = s_reverse[1:]
        # 逆序后最后一个字符为负号，则将负号放到前面来
        if s_reverse[-1] == '-':
            s_reverse = '-' + s_reverse[:-1]

        # python3中int的大小貌似基本可以认为没有边界
        # 对于其他语言，整型有边界，字符串直接转为数字可能越界报错
        num = int(s_reverse)
        minimum = -2 ** 31
        return num if minimum <= num <= 1 - minimum else 0

    def reverse1(self, x):
        # 切片[start:stop:step]，[::-1]可实现翻转
        result = ((x > 0) - (x < 0)) * int(str(abs(x))[::-1])  # int(str)可直接去掉字符串前面的0
        return result if -2 ** 31 <= result < 2 ** 31 else 0

    """
    其他语言中常见的解法为除10求余数
    但要注意python中负数除法取余与C的区别
    C、C++、Java中-12/10=-1, -12%10=-2（向零取整，余数与被除数符号相同）
    而python中-12//10=-2, -12%10=8（即divmod(-12,10)=(-2,8)，向负无穷取整，余数与除数符号相同）
    """


if __name__ == '__main__':
    print(Solution().reverse1(-10))

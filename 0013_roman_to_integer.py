# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, two is written as II in Roman numeral, just two one's added together.
# Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, the number four is written as IV.
# Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX.
# There are six instances where subtraction is used:
#
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
#
# Example 1:
#
# Input: "III"
# Output: 3
# Example 2:
#
# Input: "IV"
# Output: 4
# Example 3:
#
# Input: "IX"
# Output: 9
# Example 4:
#
# Input: "LVIII"
# Output: 58
# Explanation: C = 100, L = 50, XXX = 30 and III = 3.
# Example 5:
#
# Input: "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        for i in range(len(s) - 1):
            if roman[s[i]] >= roman[s[i + 1]]:
                num += roman[s[i]]
            else:
                # 如果当前字符比它后面紧邻的字符所代表的数字小，那么说明该字符和它后面的字符共同构成4xx或9xx，需要减去该字符所代表的值
                num -= roman[s[i]]
        # 上面的循环因为要读每个字符后面的一个元素，读取到最后一个元素i+1会越界，所以上面的循环只到倒数第二个字符
        # 最后一个字符的值在循环结束后单独加上
        num += roman[s[-1]]
        return num

    # optional: 把字符串倒过来然后考虑每个字符前面的值，与最近读到的值last作比较，这样就不用担心越界
    def romanToInt1(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        last = 0
        roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        for char in s[::-1]:
            v = roman[char]
            if v >= last:
                num += v
            else:
                num -= v
            last = v
        return num


if __name__ == '__main__':
    print(list(map(Solution().romanToInt, ["MCMXCIV", "LVIII"])))

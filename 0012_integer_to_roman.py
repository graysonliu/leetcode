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
# However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
#
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.
#
# Example 1:
#
# Input: 3
# Output: "III"
# Example 2:
#
# Input: 4
# Output: "IV"
# Example 3:
#
# Input: 9
# Output: "IX"
# Example 4:
#
# Input: 58
# Output: "LVIII"
# Explanation: C = 100, L = 50, XXX = 30 and III = 3.
# Example 5:
#
# Input: 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}
        s = str()
        divisor = 1000
        while num != 0:
            quotient, num = divmod(num, divisor)
            # 使用dict.get()，字典中不存在则返回指定默认值
            s += self.one_to_nine(quotient, roman[divisor], roman.get(divisor * 5, ''), roman.get(divisor * 10, ''))
            divisor = divisor // 10

        return s

    def one_to_nine(self, digit, char_one, char_five, char_ten):
        if digit == 9:
            return char_one + char_ten
        elif digit >= 5:
            return char_five + char_one * (digit - 5)
        elif digit == 4:
            return char_one + char_five
        else:
            return char_one * digit

    # leetcode上最快的方法。。。
    def intToRoman1(self, num):
        ONE = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        TEN = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        HUN = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        THU = ["", "M", "MM", "MMM"]
        return THU[num // 1000] + HUN[num // 100 % 10] + TEN[num // 10 % 10] + \
               ONE[num % 10]


if __name__ == '__main__':
    # map，学了要会用
    # 注意python3中的map是lazy evaluation，如果前面不加list()的话map不会执行
    print(list(map(Solution().intToRoman, [1994, 2008])))

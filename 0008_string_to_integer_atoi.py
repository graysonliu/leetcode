# Implement atoi which converts a string to an integer.
#
# The function first discards as many whitespace characters as necessary until the first non-whitespace character is found.
# Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
#
# The string can contain additional characters after those that form the integral number,
# which are ignored and have no effect on the behavior of this function.
#
# If the first sequence of non-whitespace characters in str is not a valid integral number,
# or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
#
# If no valid conversion could be performed, a zero value is returned.
#
# Note:
#
# Only the space character ' ' is considered as whitespace character.
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1].
# If the numerical value is out of the range of representable values, INT_MAX (2^31 − 1) or INT_MIN (−2^31) is returned.
# Example 1:
#
# Input: "42"
# Output: 42
# Example 2:
#
# Input: "   -42"
# Output: -42
# Explanation: The first non-whitespace character is '-', which is the minus sign.
#              Then take as many numerical digits as possible, which gets 42.
# Example 3:
#
# Input: "4193 with words"
# Output: 4193
# Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
# Example 4:
#
# Input: "words and 987"
# Output: 0
# Explanation: The first non-whitespace character is 'w', which is not a numerical
#              digit or a +/- sign. Therefore no valid conversion could be performed.
# Example 5:
#
# Input: "-91283472332"
# Output: -2147483648
# Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
#              Thefore INT_MIN (−231) is returned.

class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.lstrip()

        if not str:
            return 0

        pos = True
        if str[0] == '+' or str[0] == '-':
            pos = str[0] == '+'
            str = str[1:]

        num = 0
        for c in str:
            if '0' <= c <= '9':
                num = 10 * num + int(c)
            else:
                break
        num = num if pos else -num

        inf = 2 ** 31
        if num > inf - 1:
            return inf - 1
        elif num < -inf:
            return -inf
        else:
            return num


if __name__ == '__main__':
    print(Solution().myAtoi("-2432"))

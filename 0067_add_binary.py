# Given two binary strings, return their sum (also a binary string).
#
# The input strings are both non-empty and contains only characters 1 or 0.
#
# Example 1:
#
# Input: a = "11", b = "1"
# Output: "100"
#
# Example 2:
#
# Input: a = "1010", b = "1011"
# Output: "10101"
#
# Constraints:
#
# Each string consists only of '0' or '1' characters.
# 1 <= a.length, b.length <= 10^4
# Each string is either "0" or doesn't contain any leading zero.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        if len(a) > len(b):
            a, b = b, a
        carry = 0
        for i in range(-1, -len(a) - 1, -1):
            carry, value = divmod(int(a[i]) + int(b[i]) + carry, 2)
            result.append(str(value))
        for i in range(-len(a) - 1, -len(b) - 1, -1):
            carry, value = divmod(int(b[i]) + carry, 2)
            result.append(str(value))
        if carry == 1:
            result.append('1')
        result = ''.join(result)
        return result[::-1]


print(Solution().addBinary("1010", "1011"))

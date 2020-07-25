# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
#
# Example 1:
#
# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:
#
# Input: num1 = "123", num2 = "456"
# Output: "56088"
# Note:
#
# The length of both num1 and num2 is < 110.
# Both num1 and num2 contain only digits 0-9.
# Both num1 and num2 do not contain any leading zero, except the number 0 itself.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        digits = dict()
        l1, l2 = len(num1), len(num2)
        for i in range(l1 + l2):
            digits[i] = []
        for i, d1 in enumerate(num1[::-1]):
            for j, d2 in enumerate(num2[::-1]):
                p = int(d1) * int(d2)
                digits[i + j].append(p % 10)
                if p // 10 != 0:
                    digits[i + j + 1].append(p // 10)

        result = str()
        for i in range(l1 + l2):
            d_i = sum(digits[i])
            result = result + str(d_i % 10)
            if d_i // 10 != 0:
                digits[i + 1].append(d_i // 10)

        result = result[::-1]
        # remove leading "0"s
        for i, d in enumerate(result):
            if d != "0":
                return result[i:]

        # in case that all digits in result are "0"s
        return "0"


print(Solution().multiply("999", "999"))

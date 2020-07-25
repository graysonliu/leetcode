# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
#
# If the fractional part is repeating, enclose the repeating part in parentheses.
#
# Example 1:
#
# Input: numerator = 1, denominator = 2
# Output: "0.5"
# Example 2:
#
# Input: numerator = 2, denominator = 1
# Output: "2"
# Example 3:
#
# Input: numerator = 2, denominator = 3
# Output: "0.(6)"

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        positive = True if numerator / denominator >= 0 else False
        numerator, denominator = abs(numerator), abs(denominator)
        remainders = {}  # remainder -> the location of corresponding quotient in quotients
        quotients = []

        quotient, remainder = divmod(numerator, denominator)
        quotients.append(str(quotient) + ('.' if remainder != 0 else ''))

        while remainder != 0:
            if remainder in remainders:
                i = remainders[remainder]
                quotients[i] = '(' + quotients[i]  # repeating part starts
                quotients[-1] = quotients[-1] + ')'
                break

            remainders[remainder] = len(quotients)
            remainder *= 10
            quotient, remainder = divmod(remainder, denominator)
            quotients.append(str(quotient))

        res = ''.join(quotients)
        if not positive:
            res = '-' + res
        return res


print(Solution().fractionToDecimal(11, 9))

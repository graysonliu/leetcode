# Given a positive integer, return its corresponding column title as appear in an Excel sheet.
#
# For example:
#
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB
#     ...
# Example 1:
#
# Input: 1
# Output: "A"
# Example 2:
#
# Input: 28
# Output: "AB"
# Example 3:
#
# Input: 701
# Output: "ZY"

class Solution:
    def convertToTitle(self, n: int) -> str:
        res = []
        alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
        while n > 0:
            n -= 1  # mod 26 can only get number in [0,25], but we need it in [1,26]
            n, digit = divmod(n, 26)
            res.append(alphabet[digit])
        res.reverse()
        return ''.join(res)


print(Solution().convertToTitle(701))

# Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.

# Note:

# All letters in hexadecimal (a-f) must be in lowercase.
# The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
# The given number is guaranteed to fit within the range of a 32-bit signed integer.
# You must not use any method provided by the library which converts/formats the number to hex directly.
# Example 1:

# Input:
# 26

# Output:
# "1a"
# Example 2:

# Input:
# -1

# Output:
# "ffffffff"

class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        # get the two's complement for a number in python
        two_comp = num & 0xffffffff

        hex_digits = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
        res = []

        while two_comp != 0:
            # get last four binary digits
            last_four = two_comp & 0x0000000f
            res.append(str(last_four)
                       if 0 <= last_four <= 9
                       else hex_digits[last_four])
            # right shift
            two_comp = two_comp >> 4

        return ''.join(res)[::-1]


print(Solution().toHex(0))

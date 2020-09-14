# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
#
# Example 1:
#
# Input: 16
# Output: true
# Example 2:
#
# Input: 5
# Output: false
# Follow up: Could you solve it without loops/recursion?

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and num & (num - 1) == 0 and num & 0x55555555 != 0
        # if num is the power of 4, for its binary digits, it can only has one 1 on an odd position
        # for example, 1=0b1, 4=0b100, 16=0b10000
        # num&(num-1)==0 ensures that num only has one digit 1 and all other digits are 0
        # 5=0b0101, all digits on odd positions of 0x55555555 are 1, and others are 0
        # num&0x55555555!=0 ensures that one 1 digit of num is on odd position


print(Solution().isPowerOfFour(16))

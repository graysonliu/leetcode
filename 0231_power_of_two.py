# Given an integer, write a function to determine if it is a power of two.
#
# Example 1:
#
# Input: 1
# Output: true
# Explanation: 2^0 = 1
# Example 2:
#
# Input: 16
# Output: true
# Explanation: 2^4 = 16
# Example 3:
#
# Input: 218
# Output: false

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # my solution
        # i = 1
        # while i <= n:
        #     if i == n:
        #         return True
        #     i = i << 1
        # return False

        # trick
        # for n<=0, the result is always false
        # for n>0, if n is power of 2, then it only has one bit that is 1, and all other bits are zero
        # thus, n & (n-1) must equals to 0
        # e.g. n=32=0b100000, n-1=31=0b011111 when converted to binary digits, n&(n-1)=0
        return n & (n - 1) == 0 if n > 0 else False

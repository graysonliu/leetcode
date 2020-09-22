# Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
#
# Example 1:
#
# Input: a = 1, b = 2
# Output: 3
# Example 2:
#
# Input: a = -2, b = 3
# Output: 1

class Solution:
    def getSum(self, a: int, b: int) -> int:
        # https://en.wikipedia.org/wiki/Signed_number_representations
        # ignore carry bits, i_th bit is 1 if only one of a_i and b_i is 1, and the other is 0
        # thus, a^b is the result without carry bits
        # there is a carry in i_th bit if both a_i and b_i are 1, this carry should be added to (i+1)_th bit
        # therefore, carry bits are (a&b)<<1
        # combine a^b and the carry bits, the result should be (a^b)+((a&b)<<1)

        # both a and b are 32-bits integers
        # in python, integers could have infinite bits, we should use "& 0xffffffff" to get last 32 bits
        mask = 0xffffffff

        # this is like calling getSum(a ^ b, a & b) recursively
        while b != 0:  # if b==0, a+b=a, then a is the result
            # python also uses two's complement for negative numbers when doing bit operations
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        # out of the loop, b becomes 0 (no carry in the last iteration), and a is the result
        # if the most significant bit of a is 1, that means a is negative
        # however, python doesn't treat the most significant bit of two's complement as the sign flag (0:+, 1:-)
        # it will treat a as an unsigned integer
        # check whether the most significant bit of a is 1 (whether a is negative)
        if a >> 31 & 1 == 1:  # a is negative
            # when doing bit operations, python's behavior is just like C++ and Java
            # for example, ~(2)=~(0b00000000000000000000000000000010)=0b11111111111111111111111111111101=-3
            # 0b11111111111111111111111111111101 is the two's complement for -3
            # for any positive number n, ~(n) = -n-1
            # two's complement for negative numbers:
            # -1: 0b11111111111111111111111111111111, python treat it as 2^32-1
            # -2: 0b11111111111111111111111111111110 (subtract 1 from -1), python treat it as 2^32-2
            # -3: 0b11111111111111111111111111111101 (subtract 2 from -1), python treat it as 2^32-3
            # -4: 0b11111111111111111111111111111100 (subtract 3 from -1), python treat it as 2^32-4
            # ...
            # -2^31: 0b10000000000000000000000000000000 (subtract 2^31-1 from -1), python treat it as 2^32-2^31=2^31
            # we apply ^mask to all previous binary form, this will make all 1 to 0, and all 0 to 1
            # for a=-1 (actually 2^32-1), a^mask=0, ~(0)=-1, which happens to be exactly the result we want
            # similarly, for a=-2 (actually 2^32-2), a^mask=1, ~(1)=-2
            # ...
            # for a=-2^31 (actually 2^31), a^mask=2^31-1, ~(2^31-1)=-2^31
            # thus, the result we want is ~(a^mask)
            return ~(a ^ mask)
        else:
            return a

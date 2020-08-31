# Additive number is a string whose digits can form additive sequence.
#
# A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.
#
# Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.
#
# Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.
#
#
#
# Example 1:
#
# Input: "112358"
# Output: true
# Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5, 8.
# 1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
# Example 2:
#
# Input: "199100199"
# Output: true
# Explanation: The additive sequence is: 1, 99, 100, 199.
# 1 + 99 = 100, 99 + 100 = 199
#
#
# Constraints:
#
# num consists only of digits '0'-'9'.
# 1 <= num.length <= 35
# Follow up:
# How would you handle overflow for very large input integers?

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        # if first two elements are confirmed, then the whole sequence should be confirmed
        # since the sequence has at least three numbers, the length of the sequence can be no less than 3
        if len(num) < 3:
            return False
        # since third = first + second, the value of third should be no less than first and second
        # thus, its length in the sequence should also be no shorter than first and second
        # thus, for first and second, both their length should be at most len(num)//2
        # otherwise, their length will be larger than third
        for i in range(1, len(num) // 2 + 1):  # i denotes the length of the first number
            if num[0] == '0' and i > 1:  # heading zero, the first number can only be zero, we only need i=1 iteration
                break
            first = int(num[:i])  # first number is confirmed, it starts from index 0

            # j denotes the length of the second number
            # second number starts from index i
            # it should also be no longer than the third number
            # if i and j are confirmed, the max length of third should be len(num)-i-j
            # it should be no less than both i and j, so we have len(num)-i-j>=i and len(num)-i-j>=j
            j = 1
            while len(num) - i - j >= max(i, j):
                if num[i] == '0' and j > 1:  # heading zero, we only need j=1 iteration
                    break
                second = int(num[i:i + j])
                # then, we verify subsequent numbers
                n1, n2 = first, second
                k = i + j  # the start of subsequent numbers
                while k < len(num):
                    n3 = n1 + n2
                    n3_seq = str(n3)
                    l = len(n3_seq)
                    if k + l <= len(num) and n3_seq == num[k:k + l]:
                        k = k + l
                        n1, n2 = n2, n3
                    else:
                        break
                if k == len(num):
                    return True
                j += 1
        return False

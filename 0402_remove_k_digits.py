# Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.
#
# Note:
# The length of num is less than 10002 and will be ≥ k.
# The given num does not contain any leading zero.
# Example 1:
#
# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
# Example 2:
#
# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
# Example 3:
#
# Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with nothing which is 0.

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # solution 1
        # scan from left to right, remove the first item that is larger than its following right neighbor
        # we scan k times
        # the time complexity is O(k*n)
        L = list(num)
        for i in range(k):
            for j in range(0, len(L) - 1):
                if L[j] > L[j + 1]:
                    L.pop(j)
                    break
        res = ''.join(L)[:len(num) - k].lstrip('0')
        return res if len(res) != 0 else '0'

        # solution 2
        # using a stack with similar strategy, its time complexity is O(n)
        stack = []
        for digit in num:
            while k > 0 and len(stack) > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        res = ''.join(stack if k == 0 else stack[:-k]).lstrip('0')
        return res if len(res) != 0 else '0'


print(Solution().removeKdigits(num="10", k=2))

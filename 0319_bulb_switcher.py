# There are n bulbs that are initially off. You first turn on all the bulbs. Then, you turn off every second bulb. On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the i-th round, you toggle every i bulb. For the n-th round, you only toggle the last bulb. Find how many bulbs are on after n rounds.
#
# Example:
#
# Input: 3
# Output: 1
# Explanation:
# At first, the three bulbs are [off, off, off].
# After first round, the three bulbs are [on, on, on].
# After second round, the three bulbs are [on, off, on].
# After third round, the three bulbs are [on, off, off].
#
# So you should return 1, because there is only one bulb is on.

class Solution:
    def bulbSwitch(self, n: int) -> int:
        # my solution: bit operations (Time Limit Exceeded)
        bulbs = 0  # all bits are 0 -> all bulbs are off
        # the order of the original sequence is reversed, the last bit (least important bit) should be the first bulb
        # b xor 0 = b, b xor 1 = ~b
        for i in range(1, n + 1):
            b = 1
            for _ in range(n // i):
                b = (b << i) + 1
            b = b >> 1
            bulbs = bulbs ^ b
        # counting how many '1's in variable bulbs, i.e. how many bulbs are on
        # see #0191
        res = 0
        while bulbs != 0:
            if bulbs & 1 == 1:
                res += 1
            bulbs = bulbs >> 1
        return res

        # easier math solution
        # a bulb is on after n rounds only if it went through odd times of toggles
        # for bulb i, in the kth round, it is only toggled if i%k=0 (k is a factor of i)
        # thus, the number of different factors that i has, is also the number of times that bulb i was toggled
        # factors are always in pairs, for example, factors of 12 are: 1 and 12, 2 and 6, 3 and 4
        # but square numbers have a pair of same factors, e.g. factors of 16: 1 and 16, 2 and 8, 4 and 4
        # therefore, only square numbers have a odd number of different factors
        # then, bulb i is on after n rounds iff i is a square number
        # so, we converted this problem to finding the number of square numbers that are no larger than n
        # the answer is obviously floor(sqrt(n))
        from math import sqrt, floor
        return floor(sqrt(n))


print(Solution().bulbSwitch(3))

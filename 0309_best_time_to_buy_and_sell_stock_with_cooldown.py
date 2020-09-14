# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:
#
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
# After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
# Example:
#
# Input: [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # relevant problems: #0121, #0122
        # solution explanation: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75928/Share-my-DP-solution-(By-State-Machine-Thinking)
        # this is typically dynamic programming
        # we define three states
        # s0: you don't hold any stock, and you can buy the stock
        # s1: you have stock on you hand
        # s2: you just sold the stock, and you have to cool down for one day
        # state transfer:
        # s0 --rest--> s0
        # s0 --buy--> s1
        # s1 --rest--> s1
        # s1 --sell--> s2
        # s2 --rest--> s0
        # each day could be in one of those three states
        # suppose we don't have any money in the beginning ,the balance we have at the last day should be our profit
        # buying stock costs money and our balance could be negative, the profit is made from selling stock
        # s0[i] will be the maximum balance we have in day i if day i is in s0 state
        # s1[i] will be the maximum balance we have in day i if day i is in s1 state
        # s2[i] will be the maximum balance we have in day i if day i is in s2 state
        # s0[i]=max(s0[i-1], s2[i-1]), rest in s0, or transfer from s2 by cooling down
        # s1[i]=max(s1[i-1], s0[i-1]-prices[i]), rest in s1, or transfer from s0 by buying stock
        # s2[i]=s1[i-1]+prices[i], transfer from s1 by selling stock
        if len(prices) == 0:
            return 0
        s0, s1, s2 = ([0] * len(prices) for _ in range(3))
        # initialization
        s0[0] = 0  # we do nothing on the first day
        s1[0] = -prices[0]  # we buy stock on the first day, and our balance will be -prices[0], which is negative
        # the first day cannot be in s2 state, we have to make sure the next state cannot be transferred from s2
        # how to guarantee that? since from s2, we can only transfer to s0, and s0[i]=max(s0[i-1], s2[i-1])
        # we just need to make s2[0] smaller than s0[0] so that we choose s0[0] over s2[0] when calculating s0[1]
        # since s0[0]=0, s2[0] could be any negative number
        s2[0] = -1
        for i in range(1, len(prices)):
            s0[i] = max(s0[i - 1], s2[i - 1])
            s1[i] = max(s1[i - 1], s0[i - 1] - prices[i])
            s2[i] = s1[i - 1] + prices[i]
        # the maximum balance at the last day is the maximum profit
        # if we still have stock on our hand at the last day, the balance cannot be maximum, thus s1[-1] is ruled out
        return max(s0[-1], s2[-1])

    # the implementation above has O(n) space complexity
    # however, since we only use balances on day i-1 to calculate balances on day i
    # we can have O(1) space complexity for this approach
    # note: we can also use this approach (state machine) to solve easier problems like #0121 and #0122


print(Solution().maxProfit([1, 2, 3, 0, 2]))

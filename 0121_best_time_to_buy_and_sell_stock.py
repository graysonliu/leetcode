# Say you have an array for which the ith element is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
#
# Note that you cannot sell a stock before you buy one.
#
# Example 1:
#
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.
# Example 2:
#
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # this problem can be converted to problem 0053 (maximum subarray)
        # we first calculate the difference between adjacent numbers in the given array
        # in the difference array, find the contiguous subarray that has largest sum

        # calculate difference array
        difference = [0] * (len(prices) - 1)
        for i in range(len(prices) - 1):
            difference[i] = prices[i + 1] - prices[i]

        # find the largest sum
        max_profit = 0
        sum_ = 0
        for num in difference:
            if sum_ < 0:
                sum_ = num
            else:
                sum_ += num
            max_profit = max(max_profit, sum_)
        return max_profit

        # actually, there is a simpler one-pass solution if we don't convert it to the difference array
        # just iterating the prices array, find the minimum price along the way
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            min_price = price if price < min_price else min_price
            profit = price - min_price
            max_profit = profit if profit > max_profit else max_profit
        return max_profit

        # state machine approach inspired by #0309
        # s0: haven't bought any stock
        # s1: stock on hand
        # s2: stock sold, cannot buy stock anymore
        # s0 --rest--> s0
        # s0 --buy--> s1
        # s1 --rest--> s1
        # s1 --sell--> s2
        # s2 --rest--> s2
        # s0[i]=s0[i-1], so we don't need to update the balance value of s0 since it won't change
        # s1[i]=max(s1[i-1], s0[i-1]-prices[i])
        # s2[i]=max(s2[i-1], s1[i-1]+prices[i])
        if len(prices) == 0:
            return 0
        # initialization on day 0
        s0_balance = 0
        s1_balance = -prices[0]
        # the state at the first day cannot be s2
        # we make s2_balance small enough so that the next state cannot be transferred from s2
        s2_balance = -float('inf')
        for i in range(1, len(prices)):  # for day i
            s1_balance, s2_balance = max(s1_balance, s0_balance - prices[i]), max(s2_balance, s1_balance + prices[i])
        return max(s0_balance, s2_balance)


print(Solution().maxProfit([7, 6, 4, 3, 1]))

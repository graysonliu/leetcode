# We are playing the Guessing Game. The game will work as follows:
#
# I pick a number between 1 and n.
# You guess a number.
# If you guess the right number, you win the game.
# If you guess the wrong number, then I will tell you whether the number I picked is higher or lower, and you will continue guessing.
# Every time you guess a wrong number x, you will pay x dollars. If you run out of money, you lose the game.
# Given a particular n, return the minimum amount of money you need to guarantee a win regardless of what number I pick.
#
# Example 1:
# 
# Input: n = 10
# Output: 16
# Explanation: The winning strategy is as follows:
# - The range is [1,10]. Guess 7.
# - If this is my number, your total is $0. Otherwise, you pay $7.
# - If my number is higher, the range is [8,10]. Guess 9.
# - If this is my number, your total is $7. Otherwise, you pay $9.
# - If my number is higher, it must be 10. Guess 10. Your total is $7 + $9 = $16.
# - If my number is lower, it must be 8. Guess 8. Your total is $7 + $9 = $16.
# - If my number is lower, the range is [1,6]. Guess 3.
# - If this is my number, your total is $7. Otherwise, you pay $3.
# - If my number is higher, the range is [4,6]. Guess 5.
# - If this is my number, your total is $7 + $3 = $10. Otherwise, you pay $5.
# - If my number is higher, it must be 6. Guess 6. Your total is $7 + $3 + $5 = $15.
# - If my number is lower, it must be 4. Guess 4. Your total is $7 + $3 + $5 = $15.
# - If my number is lower, the range is [1,2]. Guess 1.
# - If this is my number, your total is $7 + $3 = $10. Otherwise, you pay $1.
# - If my number is higher, it must be 2. Guess 2. Your total is $7 + $3 + $1 = $11.
# The worst case in all these scenarios is that you pay $16. Hence, you only need $16 to guarantee a win.
# Example 2:
#
# Input: n = 1
# Output: 0
# Explanation: There is only one possible number, so you can guess 1 and not have to pay anything.
# Example 3:
#
# Input: n = 2
# Output: 1
# Explanation: There are two possible numbers, 1 and 2.
# - Guess 1.
# - If this is my number, your total is $0. Otherwise, you pay $1.
# - If my number is higher, it must be 2. Guess 2. Your total is $1.
# The worst case is that you pay $1.
#
#
# Constraints:
#
# 1 <= n <= 200

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # dynamic programming
        # dp[i][j] means search range is i~j, i<=j
        # we need to find the value of dp[1][n]
        # basic case: if i==j, dp[i][j]=0 since we only have one choice
        # other cases: iterate k from i to j (k means our guess)
        # we need to find smallest (k + max(dp[i][k-1], dp[k+1][j])), this is the minimum of the maximum
        # if k=i, it is actually k+dp[k+1][j] since dp[i][i-1] does not exist
        # if k=j, it is actually k+dp[i][k-1] since dp[j+1][j] does not exist
        # therefore, we define that dp[i][j]=0 when i is larger than j, that will not affect the result
        dp = {}

        def range_result(i, j):
            if i >= j:
                return 0
            if i + 1 == j:  # some optimization, this is like the example when n=2
                return i
            if (i, j) in dp:
                return dp[(i, j)]
            res = min(k + max(range_result(i, k - 1), range_result(k + 1, j)) for k in range(i + (j - i) // 2, j))
            # another optimization, we did not iterate k from i to j, we use i+(j-i)//2 to j-1 instead
            # k=j can be ignored since k=j-1 is always a better guess (less payment even if j is the number we picked)
            # our guesses divide the range into two ranges
            # for these two ranges, their difference of the summation of all elements in each range should be
            # as small as possible, that why we choose k in the latter half of the range

            dp[(i, j)] = res
            return res

        return range_result(1, n)

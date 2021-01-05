# You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

# Find out how many ways to assign symbols to make sum of integers equal to target S.

# Example 1:

# Input: nums is [1, 1, 1, 1, 1], S is 3.
# Output: 5
# Explanation:

# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3

# There are 5 ways to assign symbols to make the sum of nums be target 3.


# Constraints:

# The length of the given array is positive and will not exceed 20.
# The sum of elements in the given array will not exceed 1000.
# Your output answer is guaranteed to be fitted in a 32-bit integer.

from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # solution1: backtrack with memo (DP)
        memo = {}

        def backtrack(i, target):
            if i == 0:  # only the first number left
                return (1 if nums[0] == target else 0) + (1 if nums[0] == -target else 0)
            if (i, target) in memo:
                return memo[(i, target)]
            # if we choose '+' for nums[i]
            add_path = backtrack(i - 1, target - nums[i])
            # if we choose '-' for nums[i]
            sub_path = backtrack(i - 1, target + nums[i])

            memo[(i, target)] = add_path + sub_path
            return memo[(i, target)]

        return backtrack(len(nums) - 1, S)

        # solution2: convert to a subset problem (DP)
        # set A contains all numbers that we choose '+' for them
        # set B contains all numbers that we choose '-' for them
        # sum(A) - sum(B) = S
        # sum(A) = S + sum(B)
        # sum(A) + sum(A) = S + sum(A) + sum(B)
        # 2 * sum(A) = S + sum(nums)
        # sum(A) = (S + sum(nums)) / 2
        # this means we should find the number of subsets whose summation is (S + sum(nums)) / 2
        # consider numbers from index 0 to index i, we need to find subsets among those numbers, and the summation of the subset is target
        # two situations, one is putting nums[i] in the subset, another is not putting nums[i] in the subset
        # dp[i][target] = dp[i-1][target-nums[i]] + dp[i-1][target]
        memo = {}

        def dp(i, target):
            if i < 0:
                # when no numbers left and the target is 0, we've found a solution
                return 1 if target == 0 else 0
            if (i, target) in memo:
                return memo[(i, target)]
            memo[(i, target)] = dp(i - 1, target - nums[i]) + dp(i - 1, target)
            return memo[(i, target)]

        summation = sum(nums)
        if S > summation or (S + summation) % 2 == 1:
            return 0  # no solution
        return dp(len(nums) - 1, (S + summation) / 2)


print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))

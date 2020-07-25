# The set [1,2,3,...,n] contains a total of n! unique permutations.
#
# By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
#
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.
#
# Note:
#
# Given n will be between 1 and 9 inclusive.
# Given k will be between 1 and n! inclusive.
# Example 1:
#
# Input: n = 3, k = 3
# Output: "213"
# Example 2:
#
# Input: n = 4, k = 9
# Output: "2314"


class Solution:
    # solution1
    # see explanation: https://leetcode.com/problems/permutation-sequence/discuss/22507/%22Explain-like-I'm-five%22-Java-Solution-in-O(n)
    def getPermutation(self, n: int, k: int) -> str:
        result = str()
        nums = list(range(1, n + 1))
        k -= 1
        import math
        for _ in range(n):
            i, k = divmod(k, math.factorial(len(nums) - 1))
            result += str(nums.pop(i))
        return result

    # solution2: plain dfs (timeout)
    def getPermutation1(self, n: int, k: int) -> str:
        count = [0, ]

        def dfs(choices, path):
            if len(choices) == 0:
                count[0] += 1
                if count[0] == k:
                    return ''.join([str(i) for i in path])
            for i in range(len(choices)):
                candidate = choices.pop(i)
                result = dfs(choices, path + [candidate])
                if result:
                    return result
                choices.insert(i, candidate)

        return dfs(list(range(1, n + 1)), [])


print(Solution().getPermutation(3, 3))

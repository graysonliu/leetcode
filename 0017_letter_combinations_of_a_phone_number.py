# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
#
# Example:
#
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# Note:
#
# Although the above answer is in lexicographical order, your answer could be in any order you want.
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        import itertools
        return list(map(''.join, itertools.product(*(phone[d] for d in digits)))) if digits else []

        # or use reduce()
        from functools import reduce
        phone = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        return reduce(lambda l, d: [s + c for s in l for c in phone[d]], digits, ['']) if digits else []


print(Solution().letterCombinations("234"))

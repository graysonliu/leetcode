# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#
# Example 1:
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:
#
# Input: "cbbd"
# Output: "bb"
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # expand around the center
        # take each single character as the center, and expand to the left and the right at the same time
        res = ''
        for i in range(len(s)):
            left, right = i, i
            # the length of palindrome could be odd or even
            # we find continuous same characters on the right, so that we can avoid discussing these two situations
            while right + 1 < len(s) and s[right + 1] == s[i]:
                right += 1
            # expand to both directions
            while left - 1 >= 0 and right + 1 < len(s) and s[left - 1] == s[right + 1]:
                left, right = left - 1, right + 1
            if right - left + 1 > len(res):
                res = s[left:right + 1]
        return res

    # the above solution is O(n^2)

    # O(n) solution: Manacher's Algorithm
    # https://en.wikipedia.org/wiki/Longest_palindromic_substring#Manacher's_algorithm
    pass


print(Solution().longestPalindrome('cbbd'))

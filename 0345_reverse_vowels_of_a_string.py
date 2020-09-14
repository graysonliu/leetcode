# Write a function that takes a string as input and reverse only the vowels of a string.
#
# Example 1:
#
# Input: "hello"
# Output: "holle"
# Example 2:
#
# Input: "leetcode"
# Output: "leotcede"
# Note:
# The vowels does not include the letter "y".


class Solution:
    def reverseVowels(self, s: str) -> str:
        # two pointers
        vowels = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}
        s = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            left_is_vowel = s[left] in vowels
            right_is_vowel = s[right] in vowels
            if left_is_vowel and right_is_vowel:
                s[left], s[right] = s[right], s[left]
                left, right = left + 1, right - 1
            if not left_is_vowel:
                left += 1
            if not right_is_vowel:
                right -= 1
        return ''.join(s)

        # a more intuitive solution
        vowels = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}
        s = list(s)
        vowels_indices = [i for i in range(len(s)) if s[i] in vowels]
        for i in range(len(vowels_indices) // 2):
            s[vowels_indices[i]], s[vowels_indices[-i - 1]] = s[vowels_indices[-i - 1]], s[vowels_indices[i]]
        return ''.join(s)


print(Solution().reverseVowels('leetcode'))

# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
#
# Example 1:
#
# Input: 121
# Output: true
# Example 2:
#
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:
#
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# Follow up:
#
# Coud you solve it without converting the integer to a string?

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        # 不转成字符串的方法
        rev = 0
        temp = x

        while temp != 0:
            temp, remainder = divmod(temp, 10)
            rev = 10 * rev + remainder

        return x == rev

    def isPalindrome1(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # 转字符串的方法
        s = str(x)
        return s == s[::-1]

    # 一行代码
    # return str(x) == str(x)[::-1]
    # 不过str()被调用了两次，耗时长



if __name__ == '__main__':
    print(Solution().isPalindrome(121))

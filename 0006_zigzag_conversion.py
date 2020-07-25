# coding=utf-8
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string s, int numRows);
# Example 1:
#
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:
#
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
#
# P     I    N
# A   L S  I G
# Y A   H R
# P     I

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        """
        0              2n-2               4n-4
        1         2n-3 2n-1          4n-5 4n-3    
        .       .      .           .      .
        .     .        .         .        .
        n-2 n          3n-4 3n-2          5n-6
        n-1            3n-3               5n-5
        Z字型表为数组元素的索引，不考虑斜线上的元素，每一行的元素都是公差为2n-2等差数列
        而斜线上元素的索引等于同一行在它之后的元素索引减去2*(行号-1)
        例如上面的第二行，2n-3=(2n-1)-2*(2-1)，再例如第n-1行，n=(3n-4)-2*(n-1-1)
        """
        # 空字符串判断，s=''时其真值为False
        if not s or numRows == 1:
            return s

        str_to_print = str()

        # i表示行号
        for i in range(0, numRows):
            # j记录公差为2n-2的等差数列
            for j in range(i, len(s), 2 * numRows - 2):
                str_to_print += s[j]
                # 若不是第一行和最后一行，则中间存在斜线上的元素，此时还需要判断是否越界
                if i != 0 and i != numRows - 1 and j + (2 * numRows - 2) - (2 * i) < len(s):
                    str_to_print += s[j + (2 * numRows - 2) - (2 * i)]

        return str_to_print


if __name__ == "__main__":
    print(Solution().convert("PAYPALISHIRING", 3))

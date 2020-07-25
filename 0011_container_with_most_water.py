# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines,
# which together with x-axis forms a container, such that the container contains the most water.
#
# Note: You may not slant the container and n is at least 2.

# 011_container_with_most_water.jpg

# The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
# In this case, the max area of water (blue section) the container can contain is 49.

# Example:
#
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # brute force，交上去竟然超时了
        max_area = 0
        for i in range(0, len(height)):
            for j in range(i + 1, len(height)):
                max_area = max(max_area, min(height[i], height[j]) * (j - i))
        return max_area

    # 高级解法
    """
    决定面积的是区域的宽和高，宽即两个柱子之间的距离，我们希望两个柱子之间的距离越远越好
    而决定区域高的，为两个柱子的高之间的较小值，即我们希望这个较小高的值越大越好
    首先我们将宽设定为最大，即构成区域的两个柱子分别为第一个柱子和最后一个柱子
    由于决定高的是较矮的柱子，当我们想让面积变大，应该将较矮的柱子替换掉，即让区域较矮的那一边向中间移动，另一边柱子不动
    不断重复上述操作，直到两边的柱子重合
    """

    def maxArea1(self, height):
        left, right = 0, len(height) - 1
        max_area = min(height[left], height[right]) * (right - left)
        while left < right:
            h_l = height[left]
            h_r = height[right]
            # 如果左边柱子较矮，左边柱子右移
            if h_l < h_r:
                area = h_l * (right - left)
                # 接下来左边柱子需要右移，移动后area的宽变小，只有高度增加才可能得到一个更大的max_area值
                # 所以如果右移后得到的柱子高度更小，则得到的area面积必然更小，新得到的左边柱子高度也依然小于右边柱子，下次还是要移动左边
                # 所以左边柱子一直右移，直到找到一个更大高度的左边柱子
                while height[left] <= h_l and left < right:
                    left += 1
            # 反之同理
            else:
                area = h_r * (right - left)
                while height[right] <= h_r and left < right:
                    right -= 1
            max_area = max(area, max_area)
        return max_area


if __name__ == '__main__':
    print(Solution().maxArea1([1, 8, 6, 2, 5, 4, 8, 3, 7]))

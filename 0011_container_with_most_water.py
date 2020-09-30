# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
#
# Note: You may not slant the container and n is at least 2.
#
# Example:
#
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # we want the width of the area as large as possible
        # so, we start with two pointers, one at the start, another one at the end, the gap between them is the largest
        # possible width, we move these two pointers towards each other
        # how is it possible to make the area larger?
        # since the height of the area is determined by the shorter line, we should replace the shorter line
        # that is, move the pointer pointing at the shorter line towards another pointer
        res = 0
        left, right = 0, len(height) - 1
        while left < right:
            res = max(res, (right - left) * min(height[left], height[right]))
            left, right = (left + 1, right) if height[left] < height[right] else (left, right - 1)
        return res


print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))

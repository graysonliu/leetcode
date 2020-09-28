# A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.
#
# For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3) are alternately positive and negative. In contrast, [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.
#
# Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence. A subsequence is obtained by deleting some number of elements (eventually, also zero) from the original sequence, leaving the remaining elements in their original order.
#
# Example 1:
#
# Input: [1,7,4,9,2,5]
# Output: 6
# Explanation: The entire sequence is a wiggle sequence.
# Example 2:
#
# Input: [1,17,5,10,13,15,10,5,16,8]
# Output: 7
# Explanation: There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].
# Example 3:
#
# Input: [1,2,3,4,5,6,7,8,9]
# Output: 2
# Follow up:
# Can you do it in O(n) time?

from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # most likely dynamic programming
        # record the max length of any wiggle subsequence ending with nums[i]
        # but there are two situations
        # one is the difference of the last pair of numbers is positive
        # another one is the difference of the last pair of numbers is negative
        # since a sequence of length 1 is trivially wiggle sequence, we initialize with 1
        res = 0
        pos_end_len = [1] * len(nums)
        neg_end_len = [1] * len(nums)
        for i in range(0, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:  # sequence ends with positive difference nums[i]-nums[j]
                    # we should use the sequence end with nums[j] and a negative difference
                    pos_end_len[i] = max(pos_end_len[i], neg_end_len[j] + 1)
                elif nums[i] < nums[j]:
                    neg_end_len[i] = max(neg_end_len[i], pos_end_len[j] + 1)
            res = max(res, pos_end_len[i], neg_end_len[i])
        return res

        # linear DP
        # up[i] and down[i] is the length of the longest wiggle subsequence from nums[0] to nums[i] ending with a up
        # wiggle and a down wiggle respectively
        # if nums[i-1]<nums[i], it is a up wiggle, up[i]=down[i-1]+1
        # if nums[i-1]>nums[i], it is a down wiggle, down[i]=up[i-1]+1
        # since up[i] only depends on down[i-1], down[i] only depends on up[i-1], we can have a O(1) space complexity DP

        if len(nums) == 0:
            return 0
        # for i=0
        up = 1
        down = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                up = down + 1
            elif nums[i] < nums[i - 1]:
                down = up + 1

        return max(up, down)
        pass


print(Solution().wiggleMaxLength([1, 7, 4, 9, 2, 5]))

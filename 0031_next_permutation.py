# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
#
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
#
# The replacement must be in-place and use only constant extra memory.
#
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
#
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1

class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)

        if len_nums <= 1:
            return
            # return nums

        swap = False
        for i in range(len_nums - 1, 0, -1):  # 从后往前，找到第一个比它右边紧邻的数小的数nums[i-1]
            if nums[i - 1] < nums[i]:
                swap = True
                for j in range(len_nums - 1, i - 1, -1):  # 找到该数字右边比它大的最小数nums[j]，因为右边是递减的，所以直接从后往前找
                    if nums[j] > nums[i - 1]:
                        break
                break

        if swap:
            nums[j], nums[i - 1] = nums[i - 1], nums[j]  # 交换两个数字
        else:  # swap为False，表示整个序列从左往右递减，该序列为最大的全排列
            i = i - 1

        nums[i:] = nums[i:][::-1]  # nums[i-1]右侧数字颠倒
        return
        # return nums


if __name__ == '__main__':
    print(Solution().nextPermutation([2, 3, 1, 3, 3]))

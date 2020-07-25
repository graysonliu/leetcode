# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers. You may assume that each input would have exactly one solution.
#
# Example:
#
# Given array nums = [-1, 2, 1, -4], and target = 1.
#
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        # 排序后最前面三个数之和为最小和，最后面三个数相加为最大和
        min_sum = sum(nums[:3])
        max_sum = sum(nums[-3:])
        # 如果target比最大和还大，那么最大和就是最接近target的
        if target >= max_sum:
            return max_sum
        elif target <= min_sum:
            return min_sum

        # target在min_sum和max_sum之间
        # 类似于上一道题的遍历做法

        ans_sum = min_sum  # 随便给一个可能的答案

        for i in range(len(nums) - 2):
            if i == 0 or nums[i] != nums[i - 1]:  # 滤掉重复的nums[i]
                j, k = i + 1, len(nums) - 1
                while j < k:
                    current_sum = nums[i] + nums[j] + nums[k]
                    ans_sum = min(ans_sum, current_sum, key=lambda x: abs(x - target))
                    if current_sum == target:
                        return target
                    # 本次三个数之和小于target
                    elif current_sum < target:
                        # j右移增大nums[j]以使三数之和变得更大
                        j += 1
                        while j < k and nums[j] == nums[j - 1]:  # 滤掉重复的nums[j]增加效率
                            j += 1
                    # 反之
                    elif current_sum > target:
                        k -= 1
                        while j < k and nums[k] == nums[k + 1]:
                            k -= 1
        return ans_sum

    def threeSumClosest1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 改进一点
        # 前面的一样
        nums.sort()
        min_sum = sum(nums[:3])
        max_sum = sum(nums[-3:])
        if target >= max_sum:
            return max_sum
        elif target <= min_sum:
            return min_sum

        ans_sum = min_sum

        # 最快的solution没有考虑滤掉重复元素，所以我也这样直接循环了
        for i in range(len(nums) - 2):
            # 类似上面求最小和、最大和的思想，此处求包含nums[i]的最小和、最大和
            min_sum_i = nums[i] + nums[i + 1] + nums[i + 2]
            max_sum_i = nums[i] + nums[-2] + nums[-1]
            if target <= min_sum_i:
                ans_sum = min(ans_sum, min_sum_i, key=lambda x: abs(x - target))
                continue  # 找到包含nums[i]的且与target最接近的三元组之和，结束本次循环
            elif target >= max_sum_i:
                ans_sum = min(ans_sum, max_sum_i, key=lambda x: abs(x - target))
                continue
            # 否则，就还是前面的做法，引入j和k
            else:
                j, k = i + 1, len(nums) - 1
                while j < k:
                    current_sum = nums[i] + nums[j] + nums[k]
                    ans_sum = min(ans_sum, current_sum, key=lambda x: abs(x - target))
                    if current_sum < target:
                        j += 1
                    elif current_sum > target:
                        k -= 1
                    else:  # 找到等于target的
                        return target
        return ans_sum
        # 最快的solution是将中间得到的三元组之和都保存在一个list里，最后再返回与target最小的
        # 而不是每得到一个三元组的值都去和ans_sum作比较，他这样可能快一点


if __name__ == '__main__':
    print(Solution().threeSumClosest([1, 2, 4, 8, 16, 32, 64, 128], 82))

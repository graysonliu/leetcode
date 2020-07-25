# Given an array nums of n integers and an integer target, are there elements a, b, c,
# and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
#
# Note:
#
# The solution set must not contain duplicate quadruplets.
#
# Example:
#
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
#
# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]

class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 记录每个数字出现了几次
        num_count = dict()
        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1

        nums.sort()  # 排序
        two_sum = dict()  # 记录两两相加的结果
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:  # 滤掉重复元素
                for j in range(i + 1, len(nums)):
                    if j == i + 1 or nums[j] != nums[j - 1]:  # 滤掉重复元素
                        s = nums[i] + nums[j]
                        if s in two_sum:
                            two_sum[s].append((nums[i], nums[j]))
                        else:
                            two_sum[s] = [(nums[i], nums[j])]

        ans = set()

        for key in tuple(two_sum.keys()):  # 循环中用了pop，改变了字典的size，如果直接"for key in two_sum:"会报错
            if key not in two_sum:
                continue

            l1 = two_sum.pop(key)

            # 如果key=target-key的话，由于上面pop了two_sum[key]，此时two_sum[target-key]就找不到
            # 该情况下l1和l2相同
            if key != target - key and target - key not in two_sum:
                continue

            l2 = two_sum.pop(target - key) if key != target - key else l1
            for l1_t in l1:
                for l2_t in l2:
                    ans_count = dict()
                    ans_count[l1_t[0]] = ans_count.get(l1_t[0], 0) + 1
                    ans_count[l1_t[1]] = ans_count.get(l1_t[1], 0) + 1
                    ans_count[l2_t[0]] = ans_count.get(l2_t[0], 0) + 1
                    ans_count[l2_t[1]] = ans_count.get(l2_t[1], 0) + 1
                    count_flag = True
                    for num in ans_count:  # 检查是否超过了某个元素的数量
                        if ans_count[num] > num_count[num]:
                            count_flag = False
                            break
                    if count_flag:
                        """
                        依然可能存在重复的四元组
                        比如[-2,0,0,2]既可以由0+0得到（[-2,2]+[0,0]），也可以由-2+2得到（[-2,0]+[0,2]）
                        思路是利用set去重，python中set的元素，以及dict的key，只能是不可变元素，所以tuple可以加入set中，而list不行
                        突然发现leetcode对python的list和tuple没做区分
                        """
                        ans_list = [l1_t[0], l1_t[1], l2_t[0], l2_t[1]]
                        ans_list.sort()  # 排序是需要的，否则(0,0,-2,2)与(-2,0,0,2)是两个不同的tuple
                        ans.add(tuple(ans_list))

        return list(ans)

    # 通用的递归方法，无论要求几个数相加都能用
    """
    应该是动态规划？
    还是要先排序
    n个数相加等于target，假设这个n元组包含nums[i]，问题转化为n-1个数相加等于target-nums[i]
    """

    def fourSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        size = len(nums)

        if size < 4:
            return []
        if size == 4:
            if sum(nums) == target:
                return [nums]
            else:
                return []

        nums.sort()

        self.findComb(nums, size, target, ans, 0, 4, [])
        return ans

    def findComb(self, nums, size, target, ans, start, ansSize, tempAns):
        ''' recursively finding the combination. ansSize is the number of elements in the subarray'''
        if sum(nums[start:start + ansSize]) > target:
            return
        if sum(nums[-ansSize:]) < target:
            return
        if ansSize == 2:
            i = start
            j = size - 1
            while i < j:
                sigma = nums[i] + nums[j]
                if sigma > target:
                    j -= 1
                elif sigma < target:
                    i += 1
                else:
                    ans.append(tempAns + [nums[i], nums[j]])
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]:  # skip repeats
                        j -= 1
                    i += 1
                    while i < j and nums[i] == nums[i - 1]:  # skip repeats
                        i += 1
        else:
            for i in range(start, size - ansSize + 1):
                if i > start and nums[i] == nums[i - 1]:  # skip repeats
                    continue
                self.findComb(nums, size, target - nums[i], ans, i + 1, ansSize - 1, tempAns + [nums[i]])


if __name__ == '__main__':
    print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))

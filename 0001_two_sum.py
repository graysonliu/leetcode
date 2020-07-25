# coding=utf-8
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 这里的思想，将元素逐个加入到查找字典中
        # 由于没有两个元素相同，我们可以将值作为字典的key
        lookup = {}
        # enumerate()的用法，生成枚举对象，next()函数返回(count, value)元组
        # enumerate()返回的枚举对象是一个迭代器，即为一个惰性计算的序列，生成迭代器过程中不需要遍历整个list
        for i, num in enumerate(nums):
            # 判断list/tuple/set中是否存在某元素，判断dict中是否存在某key，直接用关键字in
            if target - num in lookup:
                return [lookup[target - num], i]
            lookup[num] = i


if __name__ == '__main__':
    print(Solution().twoSum((2, 7, 11, 15), 9))

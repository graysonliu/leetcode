# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.
#
# Note:
#
# The solution set must not contain duplicate triplets.
#
# Example:
#
# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 这题有些inconsistent，就拿举的例子来说，[-1,-1,2]中把两个-1当做不同的数，而[-1,0,1]又只能有一个，此时它把两个-1当做一个数
        # whatever，摊手
        # 先排序，不然到后面被去重整死了
        nums.sort()

        result = []
        # 三个数相加等于0，那么最小的数一定为负数或者为0（最小数为0时三个都是0）
        # num表示三元组中最小的数，last_i记录之前访问的数，用于去重
        last_i = None
        for i, num in enumerate(nums[:-2]):
            if num > 0:
                break
            elif num != last_i:
                last_i = num
                # 这题没有solution，看的discuss里一个同胞的解法
                j, k = i + 1, len(nums) - 1  # j为i后面紧邻的一个元素索引，k为数组最后一个元素索引
                # 始终要满足i<j<k（该条件也保证了nums[i]<=nums[j]<=nums[k]）
                while j < k:
                    last_j, last_k = nums[j], nums[k]
                    if num + nums[j] + nums[k] == 0:
                        # 找到一个解
                        result.append([num, nums[j], nums[k]])
                        # 跳过连续相等的数
                        while j < k and nums[j] == last_j:
                            j += 1
                        while j < k and nums[k] == last_k:
                            k -= 1
                    elif num + nums[j] + nums[k] < 0:
                        # 三个数相加小于0，需要增大nums[j]的值
                        while j < k and nums[j] == last_j:
                            j += 1
                    elif num + nums[j] + nums[k] > 0:
                        # 三个数相加的值大于0，需要减小nums[k]的值
                        while j < k and nums[k] == last_k:
                            k -= 1

        return result

    # leetcode上有几个特别变态的test case，上面的方法交上去会超时（欺负python慢）
    # 改进：上面的k其实不需要一个个找，因为如果nums[i]和nums[j]确定，那么nums[k]必然也确定了
    def threeSum1(self, nums):
        result = []
        # 还是要sort
        nums.sort()
        # 然后构建字典快速定位k
        # 为了满足i<j<k，字典不仅要记录元素的值，还要记录其索引
        # 同一个元素可能出现多次，即可能对应多个索引，但找到的k只需要满足i<j<k即可，k越大越好，所以我们只需要记录一个数字出现的最大索引
        nums_dict = {}
        for i, num in enumerate(nums):
            nums_dict[num] = i  # nums已经从小到大排列，所以这样记录的就是最大索引

        for i in range(0, len(nums)):
            if nums[i] > 0:
                break
            # 不用last_i的做法
            if i == 0 or nums[i] != nums[i - 1]:
                for j in range(i + 1, len(nums)):
                    if j == i + 1 or nums[j] != nums[j - 1]:  # 类似的，不用last_j
                        num_k = 0 - nums[i] - nums[j]
                        if nums_dict.get(num_k, -1) > j:  # 必须保证k>j
                            result.append([nums[i], nums[j], num_k])
        return result

    # 大神的方法，精确确定三个数各自的取值范围，仅供瞻仰
    def threeSum2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from bisect import bisect_left, bisect_right
        m = {}
        result = []

        for n in nums:
            if n in m:
                m[n] += 1
            else:
                m[n] = 1

        if 0 in m and m[0] >= 3:
            result.append([0, 0, 0])

        keys = list(m.keys())
        keys.sort()
        keys_num = len(keys)

        if keys_num == 0:
            return []

        # a<b<c，a一定小于0，c一定大于0
        end = bisect_left(keys, 0)  # a < 0
        begin = bisect_left(keys, -keys[-1] * 2)  # when b == c, a + b + c = a + 2c <= a + 2*max_c;

        for i in range(begin, end):
            a = keys[i]

            # b == c
            if a != 0 and m[a] >= 2 and -2 * a in m:
                result.append([a, a, -2 * a])

            # b的取值范围
            # -a - b = c <= keys[-1] >>>> b >= -keys[-1] - a
            min_b = -keys[-1] - a
            # b<c >>>> a + 2b < a + b + c = 0 >>>> b < -a/2
            max_b = -a / 2

            b_begin = max(i + 1, bisect_left(keys, min_b))  # b的最小值
            b_end = bisect_right(keys, max_b)  # b的最大值
            for j in range(b_begin, b_end):
                b = keys[j]
                c = -a - b
                if c in m:
                    if b > c:
                        continue
                    if b < c or m[b] >= 2:
                        result.append([a, b, c])

        return result


if __name__ == '__main__':
    print(Solution().threeSum1([-1, 0, 1, 2, -1, -4]))

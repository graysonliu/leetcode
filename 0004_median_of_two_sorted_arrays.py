# coding=utf-8
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#
# Example 1:
# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0
# Example 2:
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# The median is (2 + 3)/2 = 2.5


# coding=utf-8
# there are two sorted arrays nums1 and num2 of size m and n respectively
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
# Example 1:


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        '''
        注意两个list均已排好序，假设两个list长度之和为l
        若l为奇数，需要找到第l//2+1小的数，若l为偶数，需要找到第l/2小和第l/2+1小的数
        '''

        l = len(nums1) + len(nums2)
        if l % 2 == 1:
            return self.find_kth(nums1, nums2, l // 2 + 1)
        else:
            return (self.find_kth(nums1, nums2, l // 2) + self.find_kth(nums1, nums2, l // 2 + 1)) / 2.0

    def find_kth(self, A, B, k):
        m, n = len(A), len(B)

        '''
        找到两个已排序数组中第k小的数
        思路是，从小到大，数组A贡献i个数，那么数组B就需要贡献k-i个数（数组从0开始）
        数组A划分如下，并由此得出数组B的划分：
        ...... A[i-1]    |  A[i] ......
        ...... B[k-i-1]  |  B[k-i] ......
        需要满足A[i-1]<=B[k-i]，且B[k-i-1]<=A[i]
        由上图可知，i的取值可以是0~m共m+1种（i=0时数组A的左划分为空，i=m时数组A的右划分为空）
        第k大的数即为max(A[i-1], B[k-i-1])
        '''

        left, right = 0, m

        # 数组A的完美划分i的索引位于left和right之间
        i = (left + right) // 2

        while left < right:
            # 数组A贡献了i个，故B需要贡献k-i个
            # 我们首先需要考虑划分的合理性，如果数组B本身都没有k-i个元素，那么划分就是不合理的，A需要贡献更多个元素，即i需要无条件右移
            if k - i > n:
                # 利用二分查找的思想
                # 该情况下将左边界设定到当前位置，由i的计算公式可确保下次划分在当前位置右边
                left = i if left != i else left + 1  # 由i=(left+right)//2，如果left=right-1，那么left本身就等于i，所以left加1才能使i右移
            # 同理，如果划分使A左半边的元素数量大于k个，也不合理，i需要无条件左移
            elif i > k:
                right = i
            # 不满足A[i-1]<=B[k-i]，说明当前划分不是完美划分，完美划分在当前位置的左边，i左移
            elif i - 1 >= 0 and 0 <= k - i < n and A[i - 1] > B[k - i]:  # 首先检查数组越界
                right = i
            # 反之同理
            elif 0 <= k - i - 1 < n and i < m and B[k - i - 1] > A[i]:
                left = i if left != i else left + 1
            else:  # 已经找到完美划分
                break
            i = (left + right) // 2

        # 跳出循环后，得到完美划分
        if i == 0:  # A[i-1]不存在
            return B[k - i - 1]
        elif i == k:  # B[k-i-1]不存在
            return A[i - 1]
        else:
            return max(A[i - 1], B[k - i - 1])


if __name__ == "__main__":
    print(Solution().findMedianSortedArrays([1, 2, 3, 4, 6, 7, 8], [5]))

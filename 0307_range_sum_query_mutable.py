# Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
#
# The update(i, val) function modifies nums by updating the element at index i to val.
#
# Example:
#
# Given nums = [1, 3, 5]
#
# sumRange(0, 2) -> 9
# update(1, 2)
# sumRange(0, 2) -> 8
#
#
# Constraints:
#
# The array is only modifiable by the update function.
# You may assume the number of calls to update and sumRange function is distributed evenly.
# 0 <= i <= j <= nums.length - 1

from typing import List


class NumArray:
    # solution: segment tree
    # details: https://leetcode.com/articles/a-recursive-approach-to-segment-trees-range-sum-queries-lazy-propagation/

    def __init__(self, nums: List[int]):  # O(n)
        # we save the tree in an array, all elements in nums are leaf nodes of the tree
        # suppose len(nums)=n, then the tree has at most 2*pow(2,ceil(log2(n)))-1 nodes
        # explanation: https://stackoverflow.com/questions/28470692/how-is-the-memory-of-the-array-of-segment-tree-2-2-ceillogn-1
        # for tree node tree[i], its left child is tree[2*i+1], its right child is tree[2*i+2]
        self.n = len(nums)
        self.nums = nums
        if self.n == 0:
            return
        from math import ceil, log2
        self.tree = [0] * (2 * 2 ** ceil(log2(self.n)) - 1)
        self.build_seg_tree(0, 0, self.n - 1)

    def build_seg_tree(self, node_index, lo, hi):  # lo and hi are indices of nums
        if lo == hi:
            self.tree[node_index] = self.nums[lo]
            return
        mid = lo + (hi - lo) // 2
        # build left subtree
        self.build_seg_tree(2 * node_index + 1, lo, mid)
        # build right subtree
        self.build_seg_tree(2 * node_index + 2, mid + 1, hi)
        # merge
        self.tree[node_index] = self.tree[2 * node_index + 1] + self.tree[2 * node_index + 2]

    def update(self, i: int, val: int) -> None:
        self.update_seg_tree(0, 0, self.n - 1, i, val)

    # propagate update from the bottom to the top
    def update_seg_tree(self, node_index, lo, hi, i, val):  # O(log(n))
        if lo == hi:  # we found the leaf node that represents nums[i]
            self.tree[node_index] = val
            return
        mid = lo + (hi - lo) // 2
        if i <= mid:  # nums[i] is at left subtree
            self.update_seg_tree(2 * node_index + 1, lo, mid, i, val)
        else:  # nums[i] is at right subtree
            self.update_seg_tree(2 * node_index + 2, mid + 1, hi, i, val)
        # update parent node
        self.tree[node_index] = self.tree[2 * node_index + 1] + self.tree[2 * node_index + 2]

    def sumRange(self, i: int, j: int) -> int:
        return self.range_sum_seg_tree(0, 0, self.n - 1, i, j)

    def range_sum_seg_tree(self, node_index, lo, hi, i, j):  # O(log(n))
        if lo == i and j == hi:
            return self.tree[node_index]
        mid = lo + (hi - lo) // 2
        if j <= mid:  # the query range is on the left subtree
            return self.range_sum_seg_tree(2 * node_index + 1, lo, mid, i, j)
        if i > mid:  # the query range is on the right subtree
            return self.range_sum_seg_tree(2 * node_index + 2, mid + 1, hi, i, j)
        # the query range spans over both left subtree and right subtree
        left_sub_sum = self.range_sum_seg_tree(2 * node_index + 1, lo, mid, i, mid)
        right_sub_sum = self.range_sum_seg_tree(2 * node_index + 2, mid + 1, hi, mid + 1, j)
        return left_sub_sum + right_sub_sum


obj = NumArray([1, 3, 5])
print(obj.tree)
print(obj.sumRange(0, 2))
obj.update(1, 2)
print(obj.sumRange(0, 2))

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)

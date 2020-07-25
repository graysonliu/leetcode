#
# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
#
# Example:
#
# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 前面做过两个链表融合的，直接用那道题的方法逐个融合
    def mergeKLists1(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        from functools import reduce
        return reduce(self.merge_two_lists, lists, None)
        # 交上去超时

    # 还是用两个链表融合的方法，但不是逐个融合，而是用分治
    def mergeKLists(self, lists):
        import sys
        sys.setrecursionlimit(100000)  # 设置递归栈大小
        # leetcode上的python环境递归深度最多只能为1000，对于某些变态的test case，1000不够，所以设大点
        if not lists:
            return []
        if len(lists) == 1:
            return lists[0]
        else:
            return self.merge_two_lists(self.mergeKLists(lists[:len(lists) // 2]),
                                        self.mergeKLists(lists[len(lists) // 2:]))

    def merge_two_lists(self, l1, l2):
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.merge_two_lists(l1.next, l2)
        return l1 or l2


if __name__ == "__main__":
    l1, l1.next, l1.next.next = ListNode(1), ListNode(4), ListNode(5)
    l2, l2.next, l2.next.next = ListNode(1), ListNode(3), ListNode(4)
    l3, l3.next = ListNode(2), ListNode(6)
    lists = [l1, l2, l3]
    Solution().mergeKLists(lists)

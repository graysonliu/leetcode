# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# You may not modify the values in the list's nodes, only nodes itself may be changed.
#
# Example 1:
#
# Given 1->2->3->4, reorder it to 1->4->2->3.
# Example 2:
#
# Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

from utils import *


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # step 1: find the middle node that separate the linked list into two parts
        # step 2: reverse the latter part
        # step 3: merge these two parts

        if head is None or head.next is None:
            return
        dummy = ListNode(0, head)  # to make sure that slow end up with being the tail of the first part
        fast, slow = dummy, dummy
        while fast:
            try:
                fast = fast.next.next
            except AttributeError:
                break
            slow = slow.next

        # right now, slow should be the tail of the first part
        # reverse the second part
        cur = slow.next  # this is the head of the second part
        slow.next = None  # this is to mark the end of the first part
        pre = None
        while cur:
            next_temp = cur.next
            cur.next = pre
            pre = cur
            cur = next_temp

        # then, we merge two parts
        p1, p2 = head, pre  # pre is the head of the second part after it is reversed
        while p1:
            next_temp = p1.next
            p1.next = p2
            p1 = next_temp
            p1, p2 = p2, p1


Solution().reorderList(str_to_linked_list('1->2->3->4'))

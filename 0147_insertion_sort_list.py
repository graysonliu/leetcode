# Sort a linked list using insertion sort.
#
# Algorithm of Insertion Sort:
#
# 1. Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
# 2. At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
# 3. It repeats until no input elements remain.
#
# Example 1:
#
# Input: 4->2->1->3
# Output: 1->2->3->4
# Example 2:
#
# Input: -1->5->3->4->0
# Output: -1->0->3->4->5

from utils import ListNode


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(-float('inf'), head)
        pre_p, p = dummy, head
        while p:
            pre_q, q = None, dummy
            while q is not p:  # only check nodes before p
                if q.val > p.val:  # should insert p before q
                    pre_p.next = p.next
                    pre_q.next = p
                    p.next = q
                    p = pre_p
                    break
                pre_q = q
                q = q.next
            pre_p = p
            p = p.next

        return dummy.next

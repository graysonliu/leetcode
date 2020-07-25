# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
#
# You should preserve the original relative order of the nodes in each of the two partitions.
#
# Example:
#
# Input: head = 1->4->3->2->5->2, x = 3
# Output: 1->2->2->4->3->5
from utils import *


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy_larger, dummy_less = ListNode(0, None), ListNode(0, None)
        tail_larger, tail_less = dummy_larger, dummy_less
        p = head
        while p:
            if p.val < x:
                tail_less.next = p
                tail_less = tail_less.next
            else:
                tail_larger.next = p
                tail_larger = tail_larger.next
            p = p.next
        tail_larger.next = None
        tail_less.next = dummy_larger.next
        return dummy_less.next


h = Solution().partition(str_to_linked_list('1->4->3->2->5->2'), 3)
print(linked_list_to_str(h))

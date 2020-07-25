# Given a sorted linked list, delete all duplicates such that each element appear only once.
#
# Example 1:
#
# Input: 1->1->2
# Output: 1->2
# Example 2:
#
# Input: 1->1->2->3->3
# Output: 1->2->3

from utils import *


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, head)
        fast, slow = head, dummy
        cur = float('inf')
        while fast:
            if fast.val != cur:
                cur = fast.val
                slow.next = fast
                slow = fast
            fast = fast.next
        slow.next = None
        return dummy.next


h = Solution().deleteDuplicates(str_to_linked_list('1->1->2->3->3'))
print(linked_list_to_str(h))

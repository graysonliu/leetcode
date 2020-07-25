# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
#
# Return the linked list sorted as well.
#
# Example 1:
#
# Input: 1->2->3->3->4->4->5
# Output: 1->2->5
# Example 2:
#
# Input: 1->1->1->2->3
# Output: 2->3

from utils import *


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # dual pointers
        dummy = ListNode(0, head)
        fast, slow = head, dummy
        cur = float('inf')
        while fast:
            if fast.val != cur:
                cur = fast.val
                if not fast.next or (fast.next and fast.val != fast.next.val):
                    slow.next = fast
                    slow = fast
            fast = fast.next
        slow.next = None
        return dummy.next


h = Solution().deleteDuplicates(str_to_linked_list('1->2->2'))
print(linked_list_to_str(h))

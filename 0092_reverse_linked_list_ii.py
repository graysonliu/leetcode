# Reverse a linked list from position m to n. Do it in one-pass.
#
# Note: 1 ≤ m ≤ n ≤ length of list.
#
# Example:
#
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL

from utils import *


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # dual pointers
        dummy = ListNode(0, head)
        fast, slow = head, dummy
        count = 0
        while count < n:
            count += 1
            next_tmp = fast.next
            if count == m:
                start = fast
                pre_start = slow
            elif count > m:
                fast.next = slow
            slow = fast
            fast = next_tmp
        start.next = fast
        pre_start.next = slow
        return dummy.next


l = Solution().reverseBetween(str_to_linked_list('1->2->3->4->5'), 1, 1)
print(linked_list_to_str(l))

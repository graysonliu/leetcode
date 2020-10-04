# Given the head of a linked list, remove the nth node from the end of the list and return its head.
#
# Follow up: Could you do this in one pass?
#
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:
#
# Input: head = [1], n = 1
# Output: []
# Example 3:
#
# Input: head = [1,2], n = 1
# Output: [1]
#
#
# Constraints:
#
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz

from utils import *


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # typical two pointers
        dummy = ListNode(0, head)
        fast, slow = dummy, dummy
        i = 0
        while fast:
            fast = fast.next
            if i > n:
                slow = slow.next
            i += 1
        slow.next = slow.next.next
        return dummy.next


nums = '1->2'
print(linked_list_to_str(Solution().removeNthFromEnd(str_to_linked_list(nums), 1)))

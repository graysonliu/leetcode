# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
#
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
#
# Follow up:
#
# Could you solve the problem in O(1) extra memory space?
# You may not alter the values in the list's nodes, only nodes itself may be changed.
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
# Example 2:
#
#
# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]
# Example 3:
#
# Input: head = [1,2,3,4,5], k = 1
# Output: [1,2,3,4,5]
# Example 4:
#
# Input: head = [1], k = 1
# Output: [1]
#
#
# Constraints:
#
# The number of nodes in the list is in the range sz.
# 1 <= sz <= 5000
# 0 <= Node.val <= 1000
# 1 <= k <= sz

from utils import *


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # I don't use recursion here since the recursion stack cannot be considered as O(1) space
        dummy = ListNode(0)
        group_pre, dummy.next = dummy, head
        while True:
            p = group_pre
            for _ in range(k):  # check if there are still k nodes after group_pre
                p = p.next
                if p is None:  # it does not have k nodes to form a group, meaning this is the ending group
                    return dummy.next
            # did not return, meaning this group has k nodes, we do the reversing
            group_start, pre = group_pre.next, None
            cur = group_start
            for _ in range(k):
                next_cur = cur.next
                cur.next = pre
                pre = cur
                cur = next_cur
            # after the iteration, pre is the last node in the group
            # but it right now leads the group because of reversing
            group_pre.next = pre

            # group_start is the last node of this group after reversing
            group_start.next = cur  # after iteration, cur is the start of the next group

            group_pre = group_start


print(linked_list_to_str(Solution().reverseKGroup(str_to_linked_list('1->2->3->4->5'), 1)))

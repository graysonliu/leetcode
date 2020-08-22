# Given a singly linked list, determine if it is a palindrome.
#
# Example 1:
#
# Input: 1->2
# Output: false
# Example 2:
#
# Input: 1->2->2->1
# Output: true
# Follow up:
# Could you do it in O(n) time and O(1) space?

from utils import ListNode


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # reverse the first half
        fast, slow = head, head
        pre_slow = None
        while fast and fast.next:
            fast = fast.next.next
            slow.next, pre_slow, slow = pre_slow, slow, slow.next

        def equal_linked_list(p1, p2):
            if p1 is None and p2 is None:
                return True
            elif p1 and p2 and p1.val == p2.val:
                return equal_linked_list(p1.next, p2.next)
            else:
                return False

        if fast:  # the number of nodes is odd
            slow = slow.next
        return equal_linked_list(pre_slow, slow)

# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
#
# To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
#
# Note: Do not modify the linked list.
#
# Example 1:
#
# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the second node.
#
# Example 2:
#
# Input: head = [1,2], pos = 0
# Output: tail connects to node index 0
# Explanation: There is a cycle in the linked list, where tail connects to the first node.
#
# Example 3:
#
# Input: head = [1], pos = -1
# Output: no cycle
# Explanation: There is no cycle in the linked list.
#
# Follow-up:
# Can you solve it without using extra space?

from utils import ListNode


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # dual pointers
        # suppose when slow pointer and fast pointer meet, slow travels k steps
        # then fast travels 2k steps, since the speed of fast is twice of slow
        # head (a) -> the start node of circle (b) -> meeting node (c)
        # the route of slow: a->b->c has k steps
        # the route of fast: a->b->c->b->c has 2k steps
        # therefore, c->b->c has k steps (this is actually the length of the circle)
        # compare a->b->c and c->b->c, they both have k steps and the latter part b->c is the same
        # therefore, the length of a->b is the same as c->b
        # so, we use two pointers, one starts from a and another starts from c
        # when they meet, they are at b, the start node of the circle
        fast, slow = head, head
        while True:
            try:
                fast = fast.next.next
                slow = slow.next
            except AttributeError:
                return None  # no cycle
            if fast is slow:  # find the meeting node
                fast = head  # fast starts from head
                while fast is not slow:
                    fast = fast.next
                    slow = slow.next
                return fast

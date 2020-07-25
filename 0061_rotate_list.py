# Given a linked list, rotate the list to the right by k places, where k is non-negative.
#
# Example 1:
#
# Input: 1->2->3->4->5->NULL, k = 2
# Output: 4->5->1->2->3->NULL
# Explanation:
# rotate 1 steps to the right: 5->1->2->3->4->NULL
# rotate 2 steps to the right: 4->5->1->2->3->NULL
# Example 2:
#
# Input: 0->1->2->NULL, k = 4
# Output: 2->0->1->NULL
# Explanation:
# rotate 1 steps to the right: 2->0->1->NULL
# rotate 2 steps to the right: 1->2->0->NULL
# rotate 3 steps to the right: 0->1->2->NULL
# rotate 4 steps to the right: 2->0->1->NULL

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        # get length
        p = head
        l = 0
        while p:
            p = p.next
            l += 1
        k = k % l
        # double pointers
        p1 = head
        for _ in range(k):
            p1 = p1.next
        p2 = head
        while p1.next:
            p1 = p1.next
            p2 = p2.next
        p1.next = head
        new_head = p2.next
        p2.next = None
        return new_head
        # instead of double pointers, we can form a circle
        # then count l-k nodes from the original tail to find the split point


a, a.next, a.next.next = ListNode(0), ListNode(1), ListNode(2)
p = Solution().rotateRight(a, 4)
while p:
    print(p.val)
    p = p.next

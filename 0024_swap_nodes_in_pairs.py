# Given a linked list, swap every two adjacent nodes and return its head.
#
# Example:
#
# Given 1->2->3->4, you should return the list as 2->1->4->3.
# Note:
#
# Your algorithm should use only constant extra space.
# You may not modify the values in the list's nodes, only nodes itself may be changed.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = p = head
        p_pre = dummy
        while p and p.next:
            temp = p.next
            p_pre.next = p.next
            p.next = p.next.next  # 由于temp=p.next，思考此处会不会改变temp的值，答案当然是不会，temp是p后面的一个结点（ListNode对象的地址），此处改变的是p中指针的指向
            temp.next = p
            p_pre = p
            p = p.next
        return dummy.next

    # 递归做法
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        newhead = head.next
        head.next = self.swapPairs(head.next.next)
        newhead.next = head
        return newhead


if __name__ == "__main__":
    a, a.next, a.next.next, a.next.next.next = ListNode(1), ListNode(2), ListNode(3), ListNode(4)
    Solution().swapPairs(a)

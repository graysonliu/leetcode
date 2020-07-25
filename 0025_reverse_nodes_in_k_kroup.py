# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
#
# k is a positive integer and is less than or equal to the length of the linked list.
# If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
#
# Example:
#
# Given this linked list: 1->2->3->4->5
#
# For k = 2, you should return: 2->1->4->3->5
#
# For k = 3, you should return: 3->2->1->4->5
#
# Note:
#
# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself may be changed.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        p = head
        for _ in range(k):
            try:
                p = p.next
            except AttributeError:  # 该组的结点数不够k个，无需翻转，返回头结点
                return head

        cur = head
        pre = None  # pre为cur前面的一个结点
        for _ in range(k):  # 翻转
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        head.next = self.reverseKGroup(cur, k)  # 递归，头结点head已经变成了该组最后面的尾结点
        return pre  # pre为之前该组的尾结点，翻转后变为该组的头结点


def list_to_node(nums):
    dummy = ListNode(0)
    p = dummy
    for num in nums:
        p.next = ListNode(num)
        p = p.next
    return dummy.next


def node_to_list(p):
    nums = []
    while p:
        nums.append(p.val)
        p = p.next
    return nums


if __name__ == "__main__":
    h = list_to_node([1, 2, 3, 4, 5])
    h = Solution().reverseKGroup(h, 4)
    print(node_to_list(h))

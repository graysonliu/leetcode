# Given a linked list, remove the n-th node from the end of list and return its head.
#
# Example:
#
# Given linked list: 1->2->3->4->5, and n = 2.
#
# After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
#
# Given n will always be valid.
#
# Follow up:
#
# Could you do this in one pass?
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 自己的思路，利用字典实现one pass
        p = head
        d = dict()
        i = 0
        while p:
            d[i] = p
            i += 1
            p = p.next
        if i == n:  # 循环结束后i的值实际上为链表的长度
            return head.next
        d[i - n - 1].next = d[i - n].next
        return head

    def removeNthFromEnd1(self, head, n):
        """
        这题最容易想到的two pass思路为，先遍历一遍得到链表的长度L
        然后再从头开始，遍历到L-n个结点
        所谓的one pass做法，是用两个指针，维护一个大小为n的滑动窗口
        当前面的指针到了链表的结尾处，后面指针所指向的结点就是我们需要删除的结点
        但实际上，上面的two pass和所谓的one pass方法，它们访问结点的次数是相同的
        """
        # 链表题目的常见技巧，在最前面加一个dummy结点
        dummy = ListNode(0)
        dummy.next = head
        right = left = dummy  # 分别代表滑动窗口的左右边界
        for _ in range(n):
            right = right.next
        while right.next:
            right = right.next
            left = left.next
        left.next = left.next.next
        return dummy.next


# 用于测试

def list_to_node(nums):
    h = ListNode(nums[0])
    p = h
    for num in nums[1:]:
        p.next = ListNode(num)
        p = p.next
    return h


def node_to_list(p):
    nums = []
    while p:
        nums.append(p.val)
        p = p.next
    return nums


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    print(node_to_list(Solution().removeNthFromEnd1(list_to_node(nums), 2)))

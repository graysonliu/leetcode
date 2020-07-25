# coding=utf-8
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse
# order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        '''
        函数返回链表的第一个node，做这题时一直在纠结如何优雅的处理第一个node
        需要计算第一个node的值，但又不想在循环语句以外做多余的计算
        一个很聪明的做法，在第一个node前面再加一个dummy结点，最后返回dummy.next即可
        '''
        p = dummy = ListNode(0)
        carry = 0

        # 判断是否为None
        while l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next

            # divmod()函数同时求商和余
            # python中的特殊运算符：//表示整除，对浮点数也是整除，例如6.0//2.5=2.0；**表示求幂，例如9**0.5=3.0
            carry, val = divmod(val, 10)
            p.next = ListNode(val)
            p = p.next

        if carry == 1:
            p.next = ListNode(1)

        return dummy.next


if __name__ == '__main__':
    # 巧妙的初始化
    a, a.next, a.next.next = ListNode(2), ListNode(4), ListNode(3)
    b, b.next, b.next.next = ListNode(5), ListNode(6), ListNode(4)
    result = Solution().addTwoNumbers(a, b)
    print("{0} -> {1} -> {2}".format(result.val, result.next.val, result.next.next.val))

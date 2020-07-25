# Sort a linked list in O(n log n) time using constant space complexity.
#
# Example 1:
#
# Input: 4->2->1->3
# Output: 1->2->3->4
# Example 2:
#
# Input: -1->5->3->4->0
# Output: -1->0->3->4->5

from utils import *


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # original quick sort
        # the performance is bad on leetcode, since there is a test case that has too many same values
        # remember that the best case of quick sort is that we could divide the list into two even parts
        # the worst scenario is that the pivot we choose is the smallest or the largest (special case: all values are the same)
        # note: quick sort is unstable, while merge sort is stable, which can always achieve O(nlogn)
        def quick_sort_original(head):
            if head is None or head.next is None:  # empty or only 1 node
                return head, head
            p = head.next
            dummy1 = ListNode(0)  # leads all nodes whose values are less than or equal to head's
            dummy2 = ListNode(0)  # leads all nodes whose values are larger than head's
            p1, p2 = dummy1, dummy2
            while p:  # we choose head as the pivot
                if p.val <= head.val:
                    p1.next = p
                    p1 = p1.next
                else:
                    p2.next = p
                    p2 = p2.next
                p = p.next
            p1.next = None
            p2.next = None

            # recursion
            head1, tail1 = quick_sort_original(dummy1.next)
            head2, tail2 = quick_sort_original(dummy2.next)

            if tail1:
                tail1.next = head
            head.next = head2
            return head1 if head1 else head, tail2 if tail2 else head

        # an improved version of quick sort
        # to improve performance of the test case that has too many duplicate values
        # we divide the list into three parts, less than the pivot, equal to the pivot, larger than the pivot
        def quick_sort_improved(head):
            if head is None or head.next is None:  # empty or only 1 node
                return head, head
            p = head.next
            dummy1 = ListNode(0)  # leads all nodes whose values are less than head's
            dummy2 = ListNode(0)  # leads all nodes whose values are larger than head's
            p1, p2 = dummy1, dummy2
            p3 = head  # leads all nodes whose values are equal to head's
            while p:
                if p.val < head.val:
                    p1.next = p
                    p1 = p1.next
                elif p.val > head.val:
                    p2.next = p
                    p2 = p2.next
                else:  # equal
                    p3.next = p
                    p3 = p3.next
                p = p.next
            p1.next = None
            p2.next = None

            # recursion
            head1, tail1 = quick_sort_improved(dummy1.next)
            head2, tail2 = quick_sort_improved(dummy2.next)

            if tail1:
                tail1.next = head
            p3.next = head2
            return head1 if head1 else head, tail2 if tail2 else p3

        # merge sort, which is stable, but slightly slower than the improved version of quick sort
        def merge_sort(head):
            if head is None or head.next is None:
                return head
            # divide the list into two even parts
            dummy = ListNode(0, head)  # this is to make sure that slow ends up being the tail of the first half
            # if we start from head instead of dummy, slow will end up being the head of the second half given the code below
            slow, fast = dummy, dummy
            while True:
                try:
                    fast = fast.next.next
                    slow = slow.next
                except:
                    break

            # recursion
            head1 = merge_sort(slow.next)
            slow.next = None
            head2 = merge_sort(head)

            # merge
            p = dummy
            p1, p2 = head1, head2
            while p1 and p2:
                if p1.val <= p2.val:
                    p.next = p1
                    p1 = p1.next
                else:
                    p.next = p2
                    p2 = p2.next
                p = p.next
            p.next = p1 if p1 else p2
            return dummy.next

        # return quick_sort_original(head)[0]
        # return quick_sort_improved(head)[0]
        return merge_sort(head)


l = Solution().sortList(str_to_linked_list('4->2->1->3'))
print(linked_list_to_str(l))

# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
#
# Merge all the linked-lists into one sorted linked-list and return it.
#
#
#
# Example 1:
#
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#     1->4->5,
#           1->3->4,
#                 2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
# Example 2:
#
# Input: lists = []
# Output: []
# Example 3:
#
# Input: lists = [[]]
# Output: []
#
#
# Constraints:
#
# k == lists.length
# 0 <= k <= 10^4
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4
# lists[i] is sorted in ascending order.
# The sum of lists[i].length won't exceed 10^4.
from typing import List

from utils import *


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # using heap for k-way merge
        # heapq.merge() in python receives iterables rather than linked list
        # we can first create iterables using values of these linked lists, then use heapq.merge() to merge them
        # finally construct a new linked list using the merged iterable and return it
        # or we can implement our own version of merge() by using the PriorityQueue
        # PriorityQueue is also just a heap
        from queue import PriorityQueue
        dummy = ListNode(0)
        p = dummy
        Q = PriorityQueue()
        # from on the source code of heapq.merge(), it firstly add all heads of iterables to the heap
        for head in lists:
            if head is not None:
                Q.put((head.val, id(head), head))
                # id(node) is used as a tie breaker
                # See https://docs.python.org/3.7/library/heapq.html#priority-queue-implementation-notes
                # in above doc, it says we might need to add tuple (priority, entry count, task) to the PriorityQueue
                # the entry count serves as a tie-breaker
                # so that two tasks with the same priority are returned in the order they were added
                # that is how we guarantee sort stability
                # but we don't care sort stability here, we just need a tie-breaker
                # we use id(node) as the tie-breaker
                # if we omit id(node) and only add tuple (node.val, node) to the PriorityQueue
                # the program will encounter an error when there are two nodes with the same value (priority)
                # because our PriorityQueue lacks a tie-breaker
                pass

        while not Q.empty():
            _, _, p.next = Q.get()
            p = p.next
            if p.next is not None:
                Q.put((p.next.val, id(p.next), p.next))
        return dummy.next


l1 = str_to_linked_list('1->4->5')
l2 = str_to_linked_list('1->3->4')
l3 = str_to_linked_list('2->6')
print(linked_list_to_str(Solution().mergeKLists([l1, l2, l3])))

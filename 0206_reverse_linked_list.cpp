/*
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
        Output: 5->4->3->2->1->NULL
        Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
*/

#include "utils.h"

class Solution
{
public:
    ListNode *reverseList(ListNode *head)
    {
        ListNode *pre = nullptr, *p = head;
        while (p)
        {
            ListNode *temp_next = p->next;
            p->next = pre;
            pre = p;
            p = temp_next;
        }
        return pre;
    }
};

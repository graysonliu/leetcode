/*
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
*/

#include "utils.h"

class Solution
{
public:
    ListNode *removeElements(ListNode *head, int val)
    {
        ListNode *dummy = new ListNode(0, head);
        ListNode *p = head, *pre = dummy;
        while (p)
        {
            if (p->val == val)
                pre->next = p->next;
            else
                pre = p;
            p = p->next;
        }
        return dummy->next;
    }
};

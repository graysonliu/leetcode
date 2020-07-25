class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def str_to_linked_list(s):
    nums = s.split('->')
    dummy = ListNode(0)
    p = dummy
    for num in nums:
        p.next = ListNode(int(num))
        p = p.next
    return dummy.next


def linked_list_to_str(p):
    nums = []
    while p:
        nums.append(str(p.val))
        p = p.next
    return '->'.join(nums)

import queue


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


def list_to_tree(vals):
    Q = queue.Queue()
    root = TreeNode(vals[0])
    Q.put(root)
    i = 1
    while not Q.empty() and i < len(vals):
        node = Q.get()
        if node:
            left = TreeNode(vals[i]) if vals[i] is not None else None
            right = TreeNode(vals[i + 1]) if i + 1 < len(vals) and vals[i + 1] is not None else None
            node.left, node.right = left, right
            if left:
                Q.put(left)
            if right:
                Q.put(right)
            i += 2
    return root


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

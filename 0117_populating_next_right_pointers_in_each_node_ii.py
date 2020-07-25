# Given a binary tree
#
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
#
# Initially, all next pointers are set to NULL.
#
# Follow up:
#
# You may only use constant extra space.
# Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
#
# Example 1:
#
# Input: root = [1,2,3,4,5,null,7]
# Output: [1,#,2,3,#,4,5,7,#]
# Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
#
# Constraints:
#
# The number of nodes in the given tree is less than 6000.
# -100 <= node.val <= 100

from utils import *


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # best solution
        level_head = root
        while level_head:
            cur = level_head
            dummy = Node()  # a dummy node at the head in child level (next level)
            child_cur = dummy
            while cur:
                # first child node will be the value of dummy.next
                # dummy.next is the head of child level (next level)
                if cur.left:
                    child_cur.next = cur.left
                    child_cur = child_cur.next
                if cur.right:
                    child_cur.next = cur.right
                    child_cur = child_cur.next
                cur = cur.next
            level_head = dummy.next
        return root

        # my solution
        def find_leftmost_child_for_rightward_nodes(node):
            while node:
                if node.left:
                    return node, node.left
                if node.right:
                    return node, node.right
                node = node.next
            return None, None

        level_head = root
        while level_head:
            cur, cur_child = find_leftmost_child_for_rightward_nodes(level_head)
            next_level_head = cur_child  # the head of next level
            while cur_child:
                if cur.left == cur_child and cur.right:
                    cur_child.next = cur.right
                    cur_child = cur.right
                cur, cur_child.next = find_leftmost_child_for_rightward_nodes(cur.next)
                cur_child = cur_child.next
            level_head = next_level_head

        return root

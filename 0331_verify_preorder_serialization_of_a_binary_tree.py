# One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as #.
#
#         _9_
#        /   \
#       3     2
#      / \   / \
#     4   1  #  6
#    / \ / \   / \
#    # # # #   # #
# For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.
#
# Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree.
#
# Each comma separated value in the string must be either an integer or a character '#' representing null pointer.
#
# You may assume that the input format is always valid, for example it could never contain two consecutive commas such as "1,,3".
#
# Example 1:
#
# Input: "9,3,4,#,#,1,#,#,2,#,6,#,#"
# Output: true
# Example 2:
#
# Input: "1,#"
# Output: false
# Example 3:
#
# Input: "9,#,#,1"
# Output: false

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stack = [0]  # the first element indicates a dummy node, the number indicates its child we have visited
        nodes = preorder.split(',')
        for n in nodes:
            if len(stack) == 0:  # the dummy node was popped, that should be wrong
                return False
            stack[-1] += 1  # the top element of the stack is the parent of the current node
            if n != '#':
                stack.append(0)
            else:
                while len(stack) != 0 and stack[-1] == 2:  # we have visited both its children, so we pop it out
                    stack.pop()
        # at the end, we should have popped all nodes except the dummy node
        # and the only child of the dummy node is the root node, so stack[0] should be 1
        return len(stack) == 1 and stack[0] == 1

        # another solution without stack
        # we count available slots of the tree
        # a None node ('#') occupies one slot
        # a normal node occupies one slot, but creates two other slots in the same time
        nodes = preorder.split(',')
        slots = 1  # we have one available slot for root node initially
        for n in nodes:
            slots -= 1
            if slots < 0:
                return False
            if n != '#':
                slots += 2
        return slots == 0


print(Solution().isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))

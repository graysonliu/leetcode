# There is a list of sorted integers from 1 to n. Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.
#
# Repeat the previous step again, but this time from right to left, remove the right most number and every other number from the remaining numbers.
#
# We keep repeating the steps again, alternating left to right and right to left, until a single number remains.
#
# Find the last number that remains starting with a list of length n.
#
# Example:
#
# Input:
# n = 9,
# 1 2 3 4 5 6 7 8 9
# 2 4 6 8
# 2 6
# 6
#
# Output:
# 6

class Solution:
    def lastRemaining(self, n: int) -> int:
        # we record head, the first element of the list, after each elimination
        # if the elimination starts from the left, head will definitely be eliminated and we have to update it
        # if the elimination starts from the right, head will be eliminated only if current length is odd
        step = 1
        length = n
        head = 1
        from_left = True
        while length != 1:
            if from_left or length % 2 == 1:
                head += step
            length = length // 2
            step = step * 2
            from_left = not from_left
        return head

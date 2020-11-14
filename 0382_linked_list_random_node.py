from utils import *
import random


class Solution:
    # strategy: iterate the list, for i_th number, we choose it to replace result with probability of 1/i
    # we need to prove: for any i_th number, the probability that it is the final returned result is 1/n
    # if i_th number is the final returned result, then we have chosen it as a replacement, whose probability is 1/i
    # also, all numbers following it are not chosen, whose probability is (1-1/(i+1)) * (1-1/(i+2)) * ... * (1-1/n)
    # the probability is 1/i * i/(i+1) * (i+1)/(i+2) * ... * (n-1)/n = 1/n
    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        p = self.head
        count = 1
        while p:
            if random.randrange(count) == 0:
                res = p.val
            p = p.next
            count += 1
        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

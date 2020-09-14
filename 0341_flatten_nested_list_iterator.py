# Given a nested list of integers, implement an iterator to flatten it.
#
# Each element is either an integer, or a list -- whose elements may also be integers or other lists.
#
# Example 1:
#
# Input: [[1,1],2,[1,1]]
# Output: [1,1,2,1,1]
# Explanation: By calling next repeatedly until hasNext returns false,
# the order of elements returned by next should be: [1,1,2,1,1].
# Example 2:
#
# Input: [1,[4,[6]]]
# Output: [1,4,6]
# Explanation: By calling next repeatedly until hasNext returns false,
# the order of elements returned by next should be: [1,4,6].

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = nestedList[::-1]
        self.next_cache = None

    def next(self) -> int:
        if self.next_cache is not None:
            ret = self.next_cache
            self.next_cache = None
            return ret
        while self.stack:
            obj = self.stack.pop()
            if obj.isInteger():
                return obj.getInteger()
            else:
                self.stack.extend(obj.getList()[::-1])

    def hasNext(self) -> bool:
        if self.next_cache is not None:
            return True
        self.next_cache = self.next()
        return True if self.next_cache is not None else False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

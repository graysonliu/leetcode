# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.
#
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
#
# The cache is initialized with a positive capacity.
#
# Follow up:
# Could you do both operations in O(1) time complexity?
#
# Example:
#
# LRUCache cache = new LRUCache( 2 /* capacity */ );
#
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4

# node of double linked list
class DNode:
    def __init__(self, key: int, val: int, pre: 'DNode' = None, post: 'DNode' = None):
        self.key = key
        self.val = val
        self.pre = pre
        self.post = post


class LRUCache:
    # double linked list with traditional dict
    # we always add new node to the head of the list
    # also, every time a node is accessed, we move this node to the head
    # therefore, if the cache reaches its capacity, we always remove the tail
    def __init__(self, capacity: int):
        self.cache = dict()
        self.count = 0
        self.capacity = capacity

        # a fixed head and a fixed tail
        # new node should be added after the head
        # always remove the node before the tail
        self.head = DNode(0, 0)
        self.tail = DNode(0, 0)
        self.head.post = self.tail
        self.tail.pre = self.head

    def _add_to_head(self, node):
        node.pre = self.head
        self.cache[node.key] = node
        temp = self.head.post
        self.head.post = node
        node.post = temp
        temp.pre = node
        self.count += 1

    def _remove(self, node):
        node.post.pre = node.pre
        node.pre.post = node.post
        del self.cache[node.key]
        self.count -= 1

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_head(node)
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
            self._add_to_head(DNode(key, value))
            pass
        elif self.count == self.capacity:
            self._remove(self.tail.pre)
            self._add_to_head(DNode(key, value))
        else:
            self._add_to_head(DNode(key, value))

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

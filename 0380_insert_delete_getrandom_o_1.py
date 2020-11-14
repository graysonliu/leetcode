# Implement the RandomizedSet class:
#
# bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
# bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
# int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
# Follow up: Could you implement the functions of the class with each function works in average O(1) time?
#
#
#
# Example 1:
#
# Input
# ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
# [[], [1], [2], [2], [], [1], [2], []]
# Output
# [null, true, false, true, 2, true, false, 2]
#
# Explanation
# RandomizedSet randomizedSet = new RandomizedSet();
# randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
# randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
# randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
# randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
# randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
# randomizedSet.insert(2); // 2 was already in the set, so return false.
# randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
#
#
# Constraints:
#
# -2^31 <= val <= 2^31 - 1
# At most 105 calls will be made to insert, remove, and getRandom.
# There will be at least one element in the data structure when getRandom is called.

class RandomizedSet:
    # this problem cannot be solved by a single set, since we need to make sure getRandom() is truly random
    # set.pop() is not random
    # to make sure that getRandom is random, we still need to save those numbers in a list

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        # to remove a number in O(1), we need to find its index in O(1)
        # since there are not any duplicates, we can map a number to its index
        # when removing a number, in list, we set the last number to the removing position, then pop the last number
        self.map_to_index = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.map_to_index:
            return False
        self.map_to_index[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.map_to_index:
            return False
        # move the last number in list to the removing position
        self.map_to_index[self.nums[-1]] = self.map_to_index[val]
        self.nums[self.map_to_index[val]] = self.nums[-1]

        self.nums.pop()
        self.map_to_index.pop(val)
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        import random
        i = int(len(self.nums) * random.random())
        return self.nums[i]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

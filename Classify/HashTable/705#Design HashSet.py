# https://leetcode.com/problems/design-hashset/description/
"""
Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these functions:

add(value): Insert a value into the HashSet.
contains(value) : Return whether the value exists in the HashSet or not.
remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

Example:

MyHashSet hashSet = new MyHashSet();
hashSet.add(1);
hashSet.add(2);
hashSet.contains(1);    // returns true
hashSet.contains(3);    // returns false (not found)
hashSet.add(2);
hashSet.contains(2);    // returns true
hashSet.remove(2);
hashSet.contains(2);    // returns false (already removed)

Note:

All values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashSet library.
"""

# 使用FALSE数组构造
class MyHashSet1:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = [False] * 1000000

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.arr[key] = True

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.arr[key] = False

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return self.arr[key]

# 使用
class MyHashSet2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cap = 10000
        self.size = 0
        self.set = [None] * self.cap

    def hash(self, key):
        return key % self.cap

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        if self.contains(key):
            return

        hash_key = self.hash(key)
        if not self.set[hash_key]:
            self.set[hash_key] = []
        self.set[hash_key].append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        if not self.contains(key):
            return

        hash_key = self.hash(key)
        self.set[hash_key].remove(key)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        hash_key = self.hash(key)
        if not self.set[hash_key]:
            return False
        for k in self.set[hash_key]:
            if k == key:
                return True
        return False
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

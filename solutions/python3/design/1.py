# # 705. Design HashSet
# https://leetcode.com/problems/design-hashset/

class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None


class MyHashSet:

    def __init__(self):
        self.size = 10 ** 4
        self.arr = [ListNode(0) for i in range(self.size)]

    def add(self, key: int) -> None:
        hash = self.get_hash(key)
        curr = self.arr[hash]
        while curr.next:
            # if already exists
            if curr.next.key == key:
                return
            curr = curr.next
        curr.next = ListNode(key)

    def remove(self, key: int) -> None:
        hash = self.get_hash(key)
        curr = self.arr[hash]
        while curr.next:
            # if already exists
            if curr.next.key == key:
                curr.next = curr.next.next
        return

    def contains(self, key: int) -> bool:
        hash = self.get_hash(key)
        curr = self.arr[hash]
        while curr.next:
            # if already exists
            if curr.next.key == key:
                return True
        return False

    def get_hash(self, key):
        return key % self.size

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

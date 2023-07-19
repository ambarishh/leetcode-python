# 146. LRU Cache
# https://leetcode.com/problems/lru-cache/
# Soln- https://leetcode.com/problems/lru-cache/solutions/352295/python3-doubly-linked-list-and-dictionary/

class DLLNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keyToNodeMap = dict()
        self.head = DLLNode(-1, -1)
        self.tail = DLLNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.keyToNodeMap:
            return -1
        node = self.keyToNodeMap[key]
        self._remove(node)
        self._addToHead(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.keyToNodeMap:
            node = self.keyToNodeMap[key]
            node.val = value
            self._remove(node)
            self._addToHead(node)
        else:
            newNode = DLLNode(key, value)
            self.keyToNodeMap[key] = newNode
            self._addToHead(newNode)
            if len(self.keyToNodeMap) > self.capacity:
                self._removeFromTail()

    def _remove(self, node: DLLNode):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _addToHead(self, node: DLLNode):
        nextNode = self.head.next
        #head
        self.head.next = node
        node.prev = self.head
        #next node pointers
        node.next = nextNode
        nextNode.prev = node

    def _removeFromTail(self):
        if len(self.keyToNodeMap) == 0: return
        lastNode = self.tail.prev
        key = lastNode.key
        del self.keyToNodeMap[key]
        self._remove(lastNode)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.deque = deque()
        self.capacity = capacity
    def get(self, key: int) -> int:
        if key in self.cache:
            self.deque.remove(key)
            self.deque.appendleft(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.deque.remove(key)
        elif len(self.cache) == self.capacity:
            lru = self.deque.pop()
            del self.cache[lru]
        self.cache[key] = value
        self.deque.appendleft(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
class MyHashSet:

    def __init__(self):
        self.size = 2069
        self.arr = [-1] * self.size
    
    def _hash(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        idx =self. _hash(key)

        if self.arr[idx] >= 0:
            pass
        else:
            self.arr[idx] = key

    def remove(self, key: int) -> None:
        idx = self._hash(key)

        if self.arr[idx] < 0:
            pass
        else:
            self.arr[idx] = -1

    def contains(self, key: int) -> bool:
        idx = self._hash(key)

        if self.arr[idx] < 0:
            return False
        else:
            return True


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
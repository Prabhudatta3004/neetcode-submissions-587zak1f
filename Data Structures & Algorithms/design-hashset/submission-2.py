class MyHashSet:

    def __init__(self):
        self.size = 2069
        self.arr = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        bucket = self.arr[self._hash(key)]

        if key not in bucket:  # Avoid duplicates
            bucket.append(key)

    def remove(self, key: int) -> None:
        bucket = self.arr[self._hash(key)]

        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        bucket = self.arr[self._hash(key)]
        return key in bucket
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
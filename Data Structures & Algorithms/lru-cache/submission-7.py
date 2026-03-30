class Node:
    def __init__(self, key = 0, val = 0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hashmap = {}

    def _add_to_front(self, node):
        nxt = self.head.next
        self.head.next = node
        node.next = nxt
        node.prev = self.head
        nxt.prev = node

    def _move_to_front(self, node):
        self._remove_node(node)
        self._add_to_front(node)

    def _remove_node(self, node):
        nxt = node.next
        node.next = None
        prv = node.prev
        node.prev = None
        nxt.prev = prv
        prv.next = nxt
    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        self._move_to_front(self.hashmap[key])
        return self.hashmap[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = value
            self._move_to_front(node)
            return
       
        if len(self.hashmap) == self.capacity:
            remove_node = self.tail.prev
            del self.hashmap[remove_node.key]
            self._remove_node(remove_node)
        

        new_node = Node(key,value)
        self.hashmap[key] = new_node
        self._add_to_front(new_node)

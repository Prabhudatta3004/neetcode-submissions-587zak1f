class Node:
    def __init__(self,key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.hashmap = {}
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_to_front(self,node):
        nxt = self.head.next
        self.head.next = node
        node.prev = self.head
        nxt.prev = node
        node.next = nxt
    def _delete_node(self,node):
        nxt = node.next
        prev = node.prev
        node.next = None
        node.prev = None
        nxt.prev = prev
        prev.next = nxt
        
    def _move_to_front(self,node):
        self._delete_node(node)
        self._add_to_front(node)
    
    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]
            self._move_to_front(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = value
            self._move_to_front(node)
            return
        
        if len(self.hashmap) == self.capacity:
            del_node = self.tail.prev
            self._delete_node(del_node)
            del self.hashmap[del_node.key]
        
        new_node = Node(key,value)
        self.hashmap[key] = new_node
        self._add_to_front(new_node)

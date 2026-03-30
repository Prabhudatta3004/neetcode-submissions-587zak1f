class Node:
    def __init__(self,key=0,val=0):
        self.key=key
        self.val = val
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _add_to_front(self,node):
        next_node =self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next_node
        next_node.prev = node

    def _move_to_front(self,node):
        self._remove_node(node)
        self._add_to_front(node)
    
    def _remove_node(self,node):
        prev_node = node.prev
        next_node = node.next

        node.next = None
        node.prev = None
        
        prev_node.next = next_node
        next_node.prev = prev_node


    def get(self, key: int) -> int:
        if key in self.hashmap:
            node= self.hashmap[key]
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
            lru_node = self.tail.prev
            del self.hashmap[lru_node.key]
            self._remove_node(lru_node)

        new_node = Node(key,value)
        self._add_to_front(new_node)
        self.hashmap[key]=new_node

class Node:
    def __init__(self,key=0, value = 0):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {} ## this map has a lookup time of O(1)
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _move_to_front(self, node):
        self._remove_node(node)
        self._add_to_front(node)
    def _add_to_front(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node      # connect old first node back to new node
        self.head.next = node           # finally link head to new node

    
    def _remove_node(self,node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        
        ## but if the key exists
        ## I need to move the node to front
        ## need to update the value

        node = self.hashmap[key]
        self._move_to_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        ## case: 01 if the key exists

        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = value
            self._move_to_front(node)
            return

        ## checking if the LRU cache has reached capacity

        if len(self.hashmap) >= self.capacity:
            lru_node = self.tail.prev
            self._remove_node(lru_node)
            if lru_node.key in self.hashmap:
                del self.hashmap[lru_node.key]

        ## and add the new node, while placing it 
        ## in the front 
        new_node = Node(key,value)
        self._add_to_front(new_node)
        self.hashmap[key] = new_node



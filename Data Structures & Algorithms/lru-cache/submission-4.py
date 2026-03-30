## major functionalites
## 1. Initialize the capacity
## 2. Get function which fetches us the value, fallback to -1
## 3. if the key exists we need to update the value, if it does not exist
## we need to add the key-value ( making sure that we dont exceed the capacity)
## the key is used, MRU : 
## get and put in O(1) : get : hashmap: O(1), put:O(1): doubly LL
#
## define node: {key:value}, prev, next -- Done

class Node:
    def __init__(self, key = 0, value = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.hashmap ={}
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _move_to_front(self,node):
        self._delete_node(node)
        self._add_to_front(node)

    def _delete_node(self,node):
        ## node : prev, next
        prev_node = node.prev
        next_node = node.next

        node.next = None
        node.prev = None

        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_front(self, node):
        next_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next_node
        next_node.prev = node

    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]
            self._move_to_front(node)
            return node.value
        return -1 
        

    def put(self, key: int, value: int) -> None:
        ## if the key exists

        if key in self.hashmap:
            node = self.hashmap[key]
            node.value = value
            self._move_to_front(node)
            return
       
        ## check if we have reached capacity
        ## if we have not reached capacity 
        ## we create a new node, add it to the front
        ## create an entry in the hashmap

        
        if len(self.hashmap) == self.capacity:
            lru_node = self.tail.prev
            del self.hashmap[lru_node.key] 
            self._delete_node(lru_node)
        
        new_node = Node(key,value)
        self._add_to_front(new_node)
        self.hashmap[key] = new_node
        

class Node:
    def __init__(self,val=0):
        self.val = val
        self.next = None
class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.size = 0
        self.head = None
        self.tail = None

    def enQueue(self, value: int) -> bool:
        ## If the queue is in capacity we need to return false
        ## else add the new element to the tail

        if self.isFull():
            return False
        new_node = Node(value)
        if self.isEmpty():
            
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
        self.size +=1
        return True

    def deQueue(self) -> bool:
        
        ## if the list is empty return False

        if self.isEmpty():
            return False
        
        self.head = self.head.next
        self.size -=1

        if self.isEmpty():
            self.tail = None
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
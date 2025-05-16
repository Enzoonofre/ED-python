class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    def size(self):
        print(f"The size of the queue is {self._size}")

    def enqueue(self, value):
        new_node = Node(value)
        if self._size == 0:
            self.first = new_node
            self.last = new_node
            self._size += 1
        else:
            self.last.next = new_node
            self.last = new_node
            self._size += 1

    
    def dequeue(self):
        if self._size == 0:
            return -1
        remove_node = self.first
        self.first = self.first.next
        self._size -= 1
        if self._size == 0:
            self.last = None
        return remove_node.value


    def first_f(self):
        print(f"The first value is {self.first.value}")

    def last_f(self):
        print(f"The last value is {self.last.value}")

    def showQueue(self):
        if self._size == 0:
            print("Empty queue")
        elif self._size == 1:
            print(self.first.value)
        else:
            current_node = self.first.next
            print(self.first.value)
            while current_node:
                print("↑")
                print(current_node.value)
                current_node = current_node.next
            print("End of queue")
            print("")
        


queue = Queue()

print("Inserting elements into the queue:")
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.first_f()
queue.last_f()
queue.showQueue()

queue.size()

print("\nRemoving elements:")
print("Removed:", queue.dequeue())
print("Removed:", queue.dequeue())
queue.showQueue()

queue.size()

print("\nInserting more elements:")
queue.enqueue(40)
queue.enqueue(50)
queue.showQueue()

print("Removed:", queue.dequeue())
print("Removed:", queue.dequeue())
print("Removed:", queue.dequeue())
print("Removed (empty queue):", queue.dequeue())
queue.showQueue()
print("Final queue size:", queue.size())

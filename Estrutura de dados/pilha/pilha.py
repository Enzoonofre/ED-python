class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Pilha:
    def __init__(self):
        self.top_node = None
        self._size = 0

    def push(self,value):
        new_node = Node(value)
        new_node.next = self.top_node
        self.top_node = new_node
        self._size +=1
    
    def pop(self):
        if self.top_node is None:
            return
        self.top_node = self.top_node.next
        self._size -=1
    
    def top(self):
        if self.top_node is None:
            print("empty stack")
        print(f'The top of the stack is now {self.top_node.value}')
    
    def size(self):
        print(f"The size of stack is {self._size}")
    
    def show_stack(self):
        print("None")
        a = self.top_node
        while a:
            print("↑")
            print(a.value)
            a = a.next
        print("End of stack")
        print("")





p = Pilha()
p.push(5)
p.push(12)
p.push(8)
p.show_stack()
p.top  
print("")

print("Removing 1 iten of the stack")
p.pop()       # 8 removed
p.top     # 8
print("")

p.show_stack()
p.size() 

p.show_stack
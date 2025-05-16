class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node

        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.value, end=" -> ")
            current_node = current_node.next
        print("None")
    def inset_at(self, idx, value):
        new_node = Node(value)
        i = 0
        if idx == 0:
            new_node.next = self.head
            self.head = new_node
            current_node = self.head
        else:
            while idx != i:
                last_node = current_node
                current_node = current_node.next
                i +=1
            last_node.next = new_node
            new_node.next = current_node

    def remove(self, value):
        if self.head.value == value:
            self.head = self.head.next
        else:
            last_node = self.head
            while last_node.next.value != value:
                last_node = last_node.next
            node_remove = last_node.next
            last_node.next = node_remove.next

    
    def delete_at(self, idx):
        i = 0
        if idx ==0:
            self.head = self.head.next
        else:
            current_node = self.head
            while idx != i:
                i+=1
                last_node = current_node 
                current_node = current_node.next
            last_node.next = current_node.next
            


        


            


        


linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)

linked_list.print_list()

linked_list.delete_at(0)

linked_list.print_list()
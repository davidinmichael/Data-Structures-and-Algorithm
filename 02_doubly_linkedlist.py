class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        return True
    
    def prepend(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return new_node
    
    def pop_first(self):
        if self.length == 0:
            return False
        else:
            self.head.next.prev = None
            self.head = self.head.next
        self.length -= 1
        return True

my_doubly_linkedlist = DoublyLinkedList(1)
my_doubly_linkedlist.prepend(0)
my_doubly_linkedlist.pop_first()
my_doubly_linkedlist.print_list()
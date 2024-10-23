
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
    
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return new_node
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return new_node
    
    def insert(self, index, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            current = self.head
            for i in range(index - 1):
                prev = current
                current = current.next
            prev.next = new_node
            new_node.next = current
        self.length += 1
        return new_node
    
    def update(self, index, value):
        if not self.head:
            self.head = Node(value)
            self.tail = self.head
            self.length += 1
            return self.head
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            temp.value = value
            return True

my_linked_list = LinkedList()
my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.prepend(4)
my_linked_list.insert(3, "Inseerted")
my_linked_list.update(3, "Updated")
my_linked_list.print_list()

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
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
            self.tail = new_node
        self.length += 1
        return True
    
    def prepend(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return new_node
    
    def pop_first(self):
        if self.length == 0:
            return None
        self.head = self.head.next
        self.length -= 1
        return True
    
    def pop_last(self):
        if self.length == 0:
            return None
        if self.head.next is None:
            self.head = None
            return None
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None
        return True
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
                

my_linked_list = LinkedList(1)
# my_linked_list.print_list()
my_linked_list.append(5)
my_linked_list.prepend(0)
my_linked_list.append(6)
my_linked_list.pop_first()
my_linked_list.pop_last()
print(f"Get Node: {my_linked_list.get(1).value}")
my_linked_list.print_list()
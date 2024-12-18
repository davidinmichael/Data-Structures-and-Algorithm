
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
    
    def prepend_multiple_nodes(self, values):
        for i in reversed(values):
            self.prepend(i)
        return True
    
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
        for _ in range(index - 1):
            temp = temp.next
        return temp
    
    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index - 1):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    
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
    
    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        temp = self.head
        for _ in range(index - 1):
            temp = temp.next
        temp.next = temp.next.next
        self.length -= 1
        return True
    
    def reverse(self):
        prev = None
        current = self.head
        self.tail = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    
    def search(self, value):
        temp = self.head
        while temp:
            if temp.value == value:
                return temp.value
            temp = temp.next
        return f"{value} Not Found"

                

my_linked_list = LinkedList(5)
# my_linked_list.print_list()
# my_linked_list.append(5)
# my_linked_list.prepend(1)
# my_linked_list.append(6)
# my_linked_list.pop_first()
# my_linked_list.pop_last()
my_linked_list.prepend_multiple_nodes(values=[1, 2, 3, 4])
# print(f"Get Node: {my_linked_list.get(1).value}")
# my_linked_list.insert(1, "This is inserted")
# my_linked_list.remove(1)
# my_linked_list.reverse()
print(f"Found: {my_linked_list.search(7)}")
my_linked_list.print_list()
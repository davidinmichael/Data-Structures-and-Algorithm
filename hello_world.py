from turtle import position


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get_list(self):
        temp = self.head
        while temp:
            print(temp.value, end=" ")
            temp = temp.next
        print()

    def get_item(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        print(temp.value)
        return temp

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
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        return temp

    def pop_last(self):
        if self.length == 0:
            return None
        temp = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        pre.next = None
        self.length -= 1
        return temp

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop_last()
        else:
            prev = self.get_item(index - 1)
            temp = prev.next
            prev.next = temp.next
            temp.next = None
            self.length -= 1
            return temp

    def set_item(self, index, value):
        item = self.get_item(index)
        item.value = value
        return item

    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.prepend(value)
        temp = self.get_item(index - 1)
        next = temp.next
        temp.next = new_node
        new_node.next = next
        return new_node


my_llist = LinkedList()
my_llist.append(5)
my_llist.append(6)
my_llist.append(7)
my_llist.append(8)
my_llist.prepend(4)
# my_llist.get_list()
# my_llist.remove(2)
# my_llist.get_list()
# my_llist.pop_first()
# my_llist.get_list()
# my_llist.pop_last()
# my_llist.get_list()
# my_llist.set_item(0, 1)
my_llist.get_list()
my_llist.insert(4, 3)
my_llist.get_list()
# my_llist.get_item(3)

import time

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

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

# Initialize the linked list
ll = LinkedList(0)

# Function to time the append operation
def measure_append_time(size):
    start_time = time.time()
    for i in range(size):
        ll.append(i)
    end_time = time.time()
    return end_time - start_time

# Measure for different input sizes
for size in [1000, 10000, 100000]:
    duration = measure_append_time(size)
    print(f"Appending {size} items took {duration:.6f} seconds")

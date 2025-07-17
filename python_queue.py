class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = next

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def is_empty(self):
        return self.head is None
    
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.value
        
    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            dequeue_node = self.head
            self.head = self.head.next
            self.length -= 1
            if self.is_empty():
                self.tail = None
            return dequeue_node.value
        
# CREATE A NEW 'QUEUE' OBJECT
morning_task = Queue()

# ADD ITEMS TO THE QUEUE DURING THE PREVIOUS NIGTH
morning_task.enqueue("get dessed")
morning_task.enqueue("eat breakfast")
morning_task.enqueue("go to work")

# CHECK WHAT'LL BE YOUR FIRST TAKS DURING A MIDNIGTH WAKE-UP WITHOUT DOINT IT
morning_task.peek()

# FETCH AN ELEMENT FROM THE QUEUE IN THE MORNING RIGTH AFTER WAKING UP
task = morning_task.dequeue()

print(f"ToDo: {task}")

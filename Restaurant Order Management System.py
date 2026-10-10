# Restaurant Order Management System
# Stack and Queue using Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Stack
class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print("Order", data, "added to history.")

    def pop(self):
        if self.top is None:
            print("Order history is empty.")
            return

        print("Order", self.top.data, "removed from history.")
        self.top = self.top.next

    def display(self):
        temp = self.top
        if temp is None:
            print("Order history is empty.")
            return

        print("Order History:")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


# Queue
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)

        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        print("Order", data, "added.")

    def dequeue(self, stack):
        if self.front is None:
            print("Order queue is empty.")
            return

        data = self.front.data
        print("Preparing order:", data)

        self.front = self.front.next

        if self.front is None:
            self.rear = None

        stack.push(data)

    def display(self):
        temp = self.front

        if temp is None:
            print("Order queue is empty.")
            return

        print("Pending Orders:")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


# Main Program
stack = Stack()
queue = Queue()

while True:
    print("\n--- RESTAURANT ORDER MANAGEMENT SYSTEM ---")
    print("1. Add Order")
    print("2. Prepare Order")
    print("3. Display Pending Orders")
    print("4. Display Order History")
    print("5. Remove Latest History")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = input("Enter Food Order: ")
        queue.enqueue(data)

    elif choice == 2:
        queue.dequeue(stack)

    elif choice == 3:
        queue.display()

    elif choice == 4:
        stack.display()

    elif choice == 5:
        stack.pop()

    elif choice == 6:
        print("Program terminated.")
        break

    else:
        print("Invalid choice!")
        
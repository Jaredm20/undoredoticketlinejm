# Import the Node class you created in node.py
from node import Node

# Implement your Queue class here
class Queue:
    # Delete the following line and implement your Queue class
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None:
            # First node in queue
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return None
        value = self.front.value
        self.front = self.front.next
        if self.front is None: 
            self.rear = None
        return value

    def peek(self):
        return self.front.value if self.front else None

    def print_queue(self):
        if not self.front:
            print("(empty)")
            return
        current = self.front
        while current:
            print(f"- {current.value}")
            current = current.next
    


def run_help_desk():
    # Create an instance of the Queue class
    queue = Queue()

    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter customer name: ")
            # Add the customer to the queue
            queue.enqueue(name)
            print(f"Ticket created for: {name}")
            
            print(f"{name} added to the queue.")
        elif choice == "2":
            # Help the next customer in the queue and return message that they were helped
            customer = queue.dequeue()
            if customer:
                print(f"Serving customer:{customer}")
            else:
                print("No customers in queue")
        elif choice == "3":
            # Peek at the next customer in the queue and return their name
            customer = queue.peek()
            if customer:
                print(f"Next customer in line: {customer}")
            else:
                print("No customers in queue")
        elif choice == "4":
            # Print all customers in the queue
            print("\nWaiting customers:")
            queue.print_queue()

        elif choice == "5":
            print("Exiting Help Desk System.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_help_desk()

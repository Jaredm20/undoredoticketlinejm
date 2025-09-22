# Import the Node class you created in node.py
from node import Node

# Implement your Stack class here
class Stack:
    def __init__(self):
        self.top = None
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
    def pop(self):
        if self.top is None:
            return None
        value = self.top.value
        self.top = self.top.next
        return value
    def peek(self):
        return self.top.value if self.top else None
    def print_stack(self):
        if not self.top:
            print("(empty)")
            return
        current = self.top
        while current:
            print(f"-{current.value}")
            current = current.next
def run_undo_redo():
    # Create instances of the Stack class for undo and redo
    undo_stack = Stack()
    redo_stack = Stack()

    while True:
        print("\n--- Undo/Redo Manager ---")
        print("1. Perform action")
        print("2. Undo")
        print("3. Redo")
        print("4. View Undo Stack")
        print("5. View Redo Stack")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            action = input("Describe the action (e.g., Insert 'a'): ")
            # Push the action onto the undo stack and clear the redo stack
            undo_stack.push(action)
            redo_stack = Stack()
            print(f"Action performed: {action}")
        elif choice == "2":
            action = undo_stack.pop()
            if action:
                redo_stack.push(action)
                print(f"Action undone: {action}")
            else:
                print("Nothing to undo.")

            # Pop an action from the undo stack and push it onto the redo stack
            

        elif choice == "3":
            action = redo_stack.pop()
            if action:
                undo_stack.push(action)
                print(f"Action redone: {action}")
            else:
                print("Nothing to redo.")
            # Pop an action from the redo stack and push it onto the undo stack


        elif choice == "4":
            # Print the undo stack
            print("\nUndo Stack:")
            undo_stack.print_stack()
            

        elif choice == "5":
            # Print the redo stack
            print("\nRedo Stack:")
            redo_stack.print_stack()
            
            
        elif choice == "6":
            print("Exiting Undo/Redo Manager.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_undo_redo()

#A stack is the right choice for an undo / redo system because it’s design is more closely related to a Last-in, First-out method. This means that for problems that involve back tacking or reverse operations, a stack is the best way to go. What a LIFO behavior means is last action is the first behavior that is input is the first one to be processed. So each action is put onto a stack and allows for the user to back track easily. 
#A queue for the help desk system is a more efficient way to handle with the matter because the orders have to be handled with as them come, in order. This is more of a first-in, first-out method which means the first thing that enters into the program will be the first thing out. This program allows for each ticket to be completed in order.
#To differentiate between the stack and queue, we created our own rules for the functions rather than utilizing pythons. This is because python has more of a looser approach with append and such that does not allow for the full understanding of the stack data structure, along with the ability to manipulate items within the list rather than taking from the top. In my opinion, it also allows for easier understanding of the code and where exactly something went wrong because everything is pretty much broken down into easier parts.


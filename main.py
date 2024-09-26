class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)
        print(f"Pushed {item} to the stack.")

    def pop(self):
        if not self.is_empty():
            popped_item = self.items.pop()
            print(f"Popped {popped_item} from the stack.")
            return popped_item
        else:
            print("Stack is empty. Cannot pop.")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

    def display(self):
        print("Stack contents:", self.items)



stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

stack.display()  # Display stack contents

print("Top item is:", stack.peek())  # Peek at top item

stack.pop()  # Remove top item
stack.display()  # Display stack contents again

print("Stack size:", stack.size())  # Size of the stack

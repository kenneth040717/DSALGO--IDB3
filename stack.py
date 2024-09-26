class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def top(self):
        if self.is_empty():
            raise IndexError("top from empty stack")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)

# Example usage
S = Stack()
S.push(5)
S.push(3)
print("len(S):", len(S))  # Output: 2
print("S.pop():", S.pop())  # Output: 3
print("S.is_empty():", S.is_empty())  # Output: False
print("S.pop():", S.pop())  # Output: 5
print("S.is_empty():", S.is_empty())  # Output: True

# Uncommenting the next line will raise an error
# print("S.pop():", S.pop())  # This will raise an IndexError

S.push(7)
S.push(9)
print("S.top():", S.top())  # Output: 9
S.push(4)
print("len(S):", len(S))  # Output: 3
print("S.pop():", S.pop())  # Output: 4
S.push(6)
S.push(8)
print("S.pop():", S.pop())  # Output: 8

class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass

class Queue:
    """FIFO Queue implementation using a Python list as underlying storage."""

    def __init__(self):
        """Create an empty queue."""
        self._data = []  # nonpublic list instance

    def __len__(self):
        """Return the number of elements in the queue."""
        return len(self._data)

    def is_empty(self):
        """Return True if the queue is empty."""
        return len(self._data) == 0

    def enqueue(self, e):
        """Add element e to the back of the queue."""
        self._data.append(e)  # new item stored at end of list

    def dequeue(self):
        """
        Remove and return the first element from the queue (i.e., FIFO).
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data.pop(0)  # remove and return element from front of list

    def first(self):
        """
        Return (but do not remove) the element at the front of the queue.
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[0]  # the front element in the queue


# Example usage
q = Queue()

q.enqueue(5)
q.enqueue(3)
print(len(q))  # Output: 2
print(q.dequeue())  # Output: 5
print(q.is_empty())  # Output: False
print(q.dequeue())  # Output: 3
print(q.is_empty())  # Output: True
q.enqueue(7)
q.enqueue(9)
print(q.first())  # Output: 7
q.enqueue(4)
print(len(q))  # Output: 3
print(q.dequeue())  # Output: 7

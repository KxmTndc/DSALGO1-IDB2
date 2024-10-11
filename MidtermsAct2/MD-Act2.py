class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        return self.items.pop(0) if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0

    def first(self):
        return self.top()

    def top(self):
        return self.items[0] if not self.is_empty() else None

    def __len__(self):
        return len(self.items)

Q = Queue()

# Sequence of queue operations

Q.enqueue(5)
print("Q.enqueue:", Q.items)
Q.enqueue(3)
print("Q.enqueue:", Q.items)
print("Q.len(Q):", len(Q), Q.items)
print("Q.dequeue:", Q.dequeue(), Q.items)
print("Q.is_empty:", Q.is_empty(), Q.items)
print("Q.dequeue:", Q.dequeue(), Q.items)
print("Q.is_empty:", Q.is_empty(), Q.items)
print("Q.dequeue:", Q.dequeue(), Q.items)
Q.enqueue(7)
print("Q.enqueue:", Q.items)
Q.enqueue(9)
print("Q.enqueue:", Q.items)
print("Q.first:", Q.first(), Q.items)
Q.enqueue(4)
print("Q.enqueue:", Q.items)
print("Q.len(Q):", len(Q), Q.items)
print("Q.dequeue:", Q.dequeue(), Q.items)


print()
print("What values are returned during the following sequence of queue operations, if executed on an initially empty queue?")
Q = Queue()


Q.enqueue(5)
print("Q.enqueue:", Q.items)
Q.enqueue(3)
print("Q.enqueue:", Q.items)
print("Q.dequeue:", Q.dequeue(), Q.items)
Q.enqueue(2)
print("Q.enqueue:", Q.items)
Q.enqueue(8)
print("Q.enqueue:", Q.items)
print("Q.dequeue:", Q.dequeue(), Q.items)
print("Q.dequeue:", Q.dequeue(), Q.items)
Q.enqueue(9)
print("Q.enqueue:", Q.items)
Q.enqueue(1)
print("Q.enqueue:", Q.items)
print("Q.dequeue:", Q.dequeue(), Q.items)
Q.enqueue(7)
print("Q.enqueue:", Q.items)
Q.enqueue(6)
print("Q.enqueue:", Q.items)
print("Q.dequeue:", Q.dequeue(), Q.items)
print("Q.dequeue:", Q.dequeue(), Q.items)
Q.enqueue(4)
print("Q.enqueue:", Q.items)
print("Q.dequeue:", Q.dequeue(), Q.items)
print("Q.dequeue:", Q.dequeue(), Q.items)
print()
print("Final queue:", Q.items)
class ArrayStack:
    '''LIFO Stack implementation using a Python List
    as a data structure.'''
    def __init__(self):
        '''creating an empty stack'''
        self.data = []
    def __len__(self):
        '''return the number of elements in the stack'''
        return len(self.data)
    def is_empty(self):
        '''return True if the stack is empty'''
        return len(self) == 0
    def push(self, val):
        '''add new element to the top of the stack'''
        self.data.append(val)
    def top(self):
        '''return (but do not remove) the element at the top of the stack'''
        if self.is_empty():
            raise Exception('Stack is empty')
        return self.data[-1]
    def pop(self):
        '''remove and return the element at the top of the stack (i.e. LIFO)'''
        if self.is_empty():
            raise Exception('Stack is empty')
        return self.data.pop()


    # this is the implementation for the Queue Data Structure
    class Queue:
        DEFAULT_CAPACITY = 10

        def __init__(self):
            '''data structure size for the queue'''
            '''data structure front for the queue'''
            self._data = [None] * Queue.DEFAULT_CAPACITY
            self._size = 0
            self._front = 0

        def __len__(self):
            '''return the number of elements in the queue'''
            return self._size

        def is_empty(self):
            '''returns true if the queue is empty'''
            return self._size == 0

        def first(self):
            '''Return (but do not remove) the element at the front of the queue'''
            '''Raise an empty Exception if the queue is empty...'''
            if self.is_empty():
                raise Exception('Queue is empty')
            return self._data[self._front]

        def dequeue(self):
            '''Remove and return the first element from the queue using the FIFO structure'''
            '''Raise Empty Exception if the queue is empty'''
            if self.is_empty():
                raise Exception('Queue is empty')
            answer = self._data[self._front]
            self._data[self._front] = None
            self._front = (self._front + 1) % len(self._data)
            self._size -= 1
            return answer

        def enqueue(self, e):
            """Add an element to the back of the queue"""
            if self._size == len(self._data):
                self._resize(2 * len(self._data))
            avail = (self._front + self._size) % len(self._data)
            self._data[avail] = e
            self._size += 1

        def _resize(self, cap):
            """Resize to a new list of capacity >= len(self)"""
            old = self._data  # keep trtack of existing list
            self._data = [None] * cap  # allocate list with new capacity
            walk = self._front
            for k in range(self._size):  # only consider existing elements
                self._data[k] = old[walk]  # intentionally shift indices
                walk = (1 + walk) % len(old)  # use old size as modulus
            self._front = 0  # front has been realigned
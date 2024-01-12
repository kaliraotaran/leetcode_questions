
# FIFO


# we can use list as a queue in python

price = []

price.insert(0,123)
price.insert(0,124)
price.insert(0,125)
# this will give [125, 124, 123]

from collections import deque
q = deque()
# in queue ur always appending at left ahnd side
q.appendleft(12)
q.appendleft(13)
q.appendleft(14)
# print(q.pop())

class Queue:
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self,val):
        self.buffer.appendleft(val)
    
    def dequeue(self):
        self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)
    
pq = Queue()
pq.enqueue(12)
pq.enqueue(22)
pq.enqueue(32)
print(pq.dequeue())

class queue:
    
    def __init__(self):
        self.queue = []
        
    def enqueue(self, data):
        self.queue.append(data)
        
    def dequeue(self, data):
        
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self.queue.pop(0)
        
    def front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue[0]
    
    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)
        
        
q = queue()
q.enqueue(10)
q.dequeue(5)


            
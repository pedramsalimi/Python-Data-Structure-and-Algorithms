class Queue(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


queue = Queue()
print(queue.size())
print(queue.isEmpty())
queue.enqueue(1)
queue.enqueue(2)
dequeuedItem = queue.dequeue()
print(queue.size())
print(dequeuedItem)

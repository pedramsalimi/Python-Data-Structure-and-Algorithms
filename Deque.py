class Deque(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self,item):
        self.items.append(item)

    def addRear(self,item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

deq = Deque()
deq.addFront('Hello ')
deq.addRear('World')
print(deq.size())
print(deq.removeFront() + ' ' + deq.removeRear())
print(deq.size())
print(deq.isEmpty())

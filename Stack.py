class Stack(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


myStack = Stack()
print(myStack.isEmpty())
myStack.push(1)
myStack.push('A')
print(myStack.peek())
myStack.push(True)
print(myStack.size())
print(myStack.isEmpty())
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
print(myStack.isEmpty())

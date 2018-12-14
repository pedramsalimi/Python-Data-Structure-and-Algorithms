class DoublyLinkedListNode(object):

    def __init__(self,value):

        self.value = value
        self.next_node = None
        self.prev_node = None

a = DoublyLinkedListNode(1)
b = DoublyLinkedListNode(2)
c = DoublyLinkedListNode(3)

a.nextnode = b
b.prev_node = a
b.next_node = c
c.prev_node = b
print(b.next_node.value)

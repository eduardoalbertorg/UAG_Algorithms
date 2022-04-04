

class Node(object):
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None


class SingleLinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def insert(self, value, location):
        if value is None:
            raise ValueError
        if location > (self.size + 1):
            raise IndexError
        if location < 0:
            raise ValueError 
        if type(location) != int:
            raise TypeError
        newNode = Node(value)
        # In case there is no element yet in the Data structure
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                # Wants to store it at the beginning
                newNode.next = self.head
                self.head = newNode
            elif location == -1:
                # Wants to place it at the end
                lastNode = self.tail
                lastNode.next = newNode
                self.tail = newNode
            else:
                currentNode = self.head
                index = 0
                while index < (location - 1):
                    currentNode = currentNode.next
                    index += 1
                nextNode = currentNode.next
                currentNode.next = newNode
                newNode.next = nextNode
                if currentNode == self.tail:
                    self.tail = newNode
        self.size += 1

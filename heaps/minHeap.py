# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = []
        self.buildHeap(array)
        print(self.heap)
        
    def getLeftChildIndex(self, index):
        return 2 * index + 1
    
    def getRightChildIndex(self, index):
        return 2 * index + 2
    
    def getParentIndex(self, index):
        return (index - 1) // 2
    
    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) < len(self.heap)
    
    def hasRightChild(self, index):
        return self.getRightChildIndex(index) < len(self.heap)
    
    def hasParent(self, index):
        return self.getParentIndex(index) >= 0
    
    def leftChild(self, index):
        return self.heap[self.getLeftChildIndex(index)]
    
    def rightChild(self, index):
        return self.heap[self.getRightChildIndex(index)]
    
    def parent(self, index):
        return self.heap[self.getParentIndex(index)]

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def buildHeap(self, array):
        for element in array:
            self.insert(element)

    def siftDown(self):
        index = 0
        while self.hasLeftChild(index):
            smallerChildIndex = self.getLeftChildIndex(index)

            if self.hasRightChild(index) and self.rightChild(index) < self.leftChild(index):
                smallerChildIndex = self.getRightChildIndex(index)
            
            if self.heap[index] > self.heap[smallerChildIndex]:
                print('Swapping', self.heap[index], 'with', self.heap[smallerChildIndex])
                self.swap(index, smallerChildIndex)
                
            index = smallerChildIndex

    def siftUp(self):
        index = len(self.heap) - 1
        while self.hasParent(index) and self.parent(index) > self.heap[index]:
            self.swap(self.getParentIndex(index), index)
            index = self.getParentIndex(index)

    def peek(self):
        return self.heap[0]

    def remove(self):
        lastIndex = len(self.heap) - 1
        self.swap(0, lastIndex)
        minimumValue = self.heap.pop()
        self.siftDown()
        return minimumValue

    def insert(self, value):
        self.heap.append(value)
        self.siftUp()
        

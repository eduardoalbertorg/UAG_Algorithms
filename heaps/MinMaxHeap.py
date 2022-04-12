class Heap(object):
    def __init__(self, comparisonFunc, array):
        self.comparisonFunc = comparisonFunc
        self.heap = []
        self.buildHeap(array)
    
    def getSize(self):
        return len(self.heap)
    
    def getArray(self):
        return self.heap
        
    def getLeftChildIndex(self, index):
        return 2 * index + 1
    
    def getRightChildIndex(self, index):
        return 2 * index + 2
    
    def getParentIndex(self, index):
        return (index - 1) // 2
    
    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) < self.getSize()
    
    def hasRightChild(self, index):
        return self.getRightChildIndex(index) < self.getSize()
    
    def hasParent(self, index):
        return self.getParentIndex(index) >= 0
    
    def leftChild(self, index):
        return self.heap[self.getLeftChildIndex(index)]
    
    def rightChild(self, index):
        return self.heap[self.getRightChildIndex(index)]
    
    def parent(self, index):
        return self.heap[self.getParentIndex(index)]
    
    # O(n) time | O(1) space
    def buildHeap(self, array):
        for element in array:
            self.insert(element)

    # O(log(n)) time | O(1) space        
    def siftUp(self):
        index = len(self.heap) - 1
        parentIndex = self.getParentIndex(index)
        while self.hasParent(index) and self.comparisonFunc(self.heap[index], self.heap[parentIndex]):
            self.swap(index, parentIndex)
            index = parentIndex
            parentIndex = self.getParentIndex(index)
                
    # O(log(n)) time | O(1) space
    def siftDown(self):
        index = 0
        while self.hasLeftChild(index):
            leftChildIndex = self.getLeftChildIndex(index)
            rightChildIndex = self.getRightChildIndex(index)
            indexToSwap = leftChildIndex
            
            if self.hasRightChild(index) and self.comparisonFunc(self.heap[rightChildIndex], self.heap[leftChildIndex]):
                indexToSwap = rightChildIndex

            if self.comparisonFunc(self.heap[indexToSwap], self.heap[index]):
                self.swap(index, indexToSwap)
            index = indexToSwap
                
    # O(log(n)) time | O(1) space
    def insert(self, value):
        self.heap.append(value)
        self.siftUp()
        
    # O(log(n)) time | O(1) space
    def remove(self):
        self.swap(0, len(self.heap) - 1)
        valueToRemove = self.heap.pop()
        self.siftDown()
        return valueToRemove
    
    # O(1) time | O(1) space
    def peek(self):
        return self.heap[0]
    
    # O(1) time | O(1) space
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

# END HEAP CLASS		
        
def MAX_HEAP_FUNC(a, b):
    print(f'#### Is {a} greater than {b}')
    return a > b

def MIN_HEAP_FUNC(a, b):
    print(f'#### Is {a} lesser than {b}')
    return a < b
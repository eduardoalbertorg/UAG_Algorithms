class Heap(object):
    def __init__(self, comparisonFunc, array):
        self.comparisonFunc = comparisonFunc
        self.heap = []
        self.buildHeap(array)
        
    def getLeftChildIndex(self, index):
        return 2 * index + 1
    
    def getRightChildIndex(self, index):
        return 2 * index + 2
    
    def getParentIndex(self, index):
        return (index - 1) // 2
    
    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) < len(self.heap)
    
    def hasLeftChild(self, index):
        return self.getRightChildIndex(index) < len(self.heap)
    
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
        print(self.heap)
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
            
            if self.hasRightChild(index):
                rightChildIndex = self.getRightChildIndex(index)
                if self.comparisonFunc(self.heap[leftChildIndex], self.heap[rightChildIndex]):
                    indexToSwap = leftChildIndex
                else:
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
        self.swap(0, len(self.heap))
        valueToRemove = self.heap.pop()
        self.siftDown()
        return valueToRemove

    # O(1) time | O(1) space           
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

# END HEAP CLASS		
        
def MAX_HEAP_FUNC(a, b):
    return a > b

def MIN_HEAP_FUNC(a, b):
    return a < b
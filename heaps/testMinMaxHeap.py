import unittest
from MinMaxHeap import Heap
from MinMaxHeap import MAX_HEAP_FUNC
from MinMaxHeap import MIN_HEAP_FUNC


def isMinHeapPropertySatisfied(array):
    for currentIdx in range(1, len(array)):
        parentIdx = (currentIdx - 1) // 2
        if array[parentIdx] > array[currentIdx]:
            return False
    return True

def isMaxHeapPropertySatisfied(array):
    for currentIdx in range(1, len(array)):
        parentIdx = (currentIdx - 1) // 2
        if array[parentIdx] < array[currentIdx]:
            return False
    return True


class TestMinMaxHeap(unittest.TestCase):
    
    def test_case_1_min_heap(self):
        array = [15, 20, 9, 13, 10, 7, 9, 8, 4, 3]
        minHeap = Heap(MIN_HEAP_FUNC, array)
        print(minHeap.heap)
        print(isMinHeapPropertySatisfied(minHeap.heap))
        self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))
        """handler = program.ContinuousMedianHandler()
        handler.insert(5)
        handler.insert(10)
        self.assertEqual(handler.getMedian(), 7.5)
        handler.insert(100)
        self.assertEqual(handler.getMedian(), 10)
        """

    def test_case_1_max_heap(self):
        array = [15, 20, 9, 13, 10, 7, 9, 8, 4, 3]
        maxHeap = Heap(MAX_HEAP_FUNC, array)
        print(maxHeap.heap)
        print(isMaxHeapPropertySatisfied(maxHeap.heap))
        self.assertTrue(isMaxHeapPropertySatisfied(maxHeap.heap))

if __name__ == '__main__':
    unittest.main()
from lib2to3.pytree import Node
import unittest
from single_linked_list import Node
from single_linked_list import SingleLinkedList

class TestSingleLinkedList(unittest.TestCase):

    def test_insert_1_element(self):
        singleLinkedList = SingleLinkedList()
        singleLinkedList.insert(6, 0)
        self.assertEqual(singleLinkedList.size, 1)

    def test_insert_2_elements(self):
        singleLinkedList = SingleLinkedList()
        singleLinkedList.insert(6, 0)
        singleLinkedList.insert(7, 0)
        self.assertEqual(singleLinkedList.size, 2)

    def test_insert_location_greater_than_size(self):
        with self.assertRaises(IndexError):
            singleLinkedList = SingleLinkedList()
            singleLinkedList.insert(6, 2)

    def test_insert_valid_location(self):
        singleLinkedList = SingleLinkedList()
        singleLinkedList.insert(6, 1)
        self.assertEqual(singleLinkedList.size, 1)

    def test_wrong_location_data_type(self):
        with self.assertRaises(TypeError):
            singleLinkedList = SingleLinkedList()
            singleLinkedList.insert(6, "1")

    def test_negative_location(self):
        with self.assertRaises(ValueError):
            singleLinkedList = SingleLinkedList()
            singleLinkedList.insert(6, -1)
        

    def test_none_value(self):
        with self.assertRaises(ValueError):
            singleLinkedList = SingleLinkedList()
            singleLinkedList.insert(None, 0)
    

if __name__ == '__main__':
    unittest.main()
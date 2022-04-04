class DLinkedNode():
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None

class LRUCache():
    
    def _add_node(self, node):
        # Adds the new node right after the head
        node.prev = self.head
        node.next = self.head.next
        
        self.head.next.prev = node
        self.head.next = node
        
    def _remove_node(self, node):
        prev = node.prev
        new = node.next
        
        prev.next = new
        new.prev = prev
        
    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)
        
    def _pop_tail(self):
        """
        Pop the current tail
        """
        res = self.tail.prev
        self._remove_node(res)
        return res

    def __init__(self, capacity: int):
        self.cache_dict = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = DLinkedNode(), DLinkedNode()
        
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        # If the vaulue doesn't exists, returns a 'None' value or specified in second arg
        node = self.cache_dict.get(key, None)
        if not node:
            return -1
        # Move the accesed node to the head
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.cache_dict.get(key)
        
        if not node:
            new_node = DLinkedNode()
            new_node.key = key
            new_node.value = value
            
            self.cache_dict[key] = new_node
            self._add_node(new_node)
            
            self.size += 1
            
            if self.size > self.capacity:
                # Pop the tail
                tail = self._pop_tail()
                del self.cache_dict[tail.key]
                self.size -= 1
        else:
            # Update the value
            node.value = value
            self._move_to_head(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
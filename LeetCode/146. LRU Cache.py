# expected solution on interview
# double linked list(LRU) + hash(cache)
# head is used recently, so tail will be removed
class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = dict() # key to node
        self.capacity = capacity
        self.head = ListNode(0, 0)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove_from_list(node)
            self.insert_after_head(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:                
            node = self.cache[key]
            self.remove_from_list(node)
            self.insert_after_head(node)
            node.value = value       
        else: 
            if len(self.cache) >= self.capacity:
                del self.cache[self.tail.prev.key]
                self.remove_from_list(self.tail.prev)
            node = ListNode(key, value)
            self.cache[key] = node
            self.insert_after_head(node)
			
    def remove_from_list(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def insert_after_head(self, node):
        head_next = self.head.next 
        self.head.next = node 
        node.prev = self.head 
        node.next = head_next 
        head_next.prev = node


# simple solution with ordered dict
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = OrderedDict()
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key) 
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if len(self.cache) >= self.size:
                self.cache.popitem(last=False) 
        else:
            self.cache.move_to_end(key)
        self.cache[key] = value
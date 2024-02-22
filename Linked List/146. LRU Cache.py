# 146. LRU Cache

class ListNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = defaultdict(int)
        self.capacity = capacity
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def update_cache(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = self.tail.prev
        self.tail.prev.next = node
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.update_cache(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.update_cache(node)
        else:
            if len(self.cache) == self.capacity:
                node = self.head.next
                del self.cache[node.key]
                self.head.next = node.next
                node.next.prev = self.head

            new_node = ListNode(key, value)
            self.cache[key] = new_node
            new_node.prev = self.tail.prev
            self.tail.prev.next = new_node  
            new_node.next = self.tail
            self.tail.prev = new_node       


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
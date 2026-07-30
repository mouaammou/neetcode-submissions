class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity

        self.cache = {} # key : node

        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev_node = node.prev

        node_next = node.next

        prev_node.next = node_next
        node_next.prev = prev_node
    
    def insert(self, node):
        prev_node = self.right.prev

        prev_node.next = node 

        node.prev = prev_node
        node.next = self.right

        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]

        self.remove(node)
        self.insert(node)

        return node.value
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next

            self.remove(lru)

            del self.cache[lru.key]

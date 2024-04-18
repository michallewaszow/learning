class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.hash_table = [Node(0) for i in range(10000)]

    def add(self, key: int) -> None:
        hash = key % len(self.hash_table)
        node = self.hash_table[hash]
        while node.next:
            if node.next.key == key:
                return
            node = node.next
        node.next = Node(key)
            
        

    def remove(self, key: int) -> None:
        hash = key % len(self.hash_table)
        node = self.hash_table[hash]
        while node.next:
            if node.next.key == key:
                node.next = node.next.next
                return
            node = node.next
                

    def contains(self, key: int) -> bool:
        hash = key % len(self.hash_table)
        node = self.hash_table[hash]
        while node.next:
            if node.next.key == key:
                return True
            node = node.next
        return False

# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
print(obj.add(1))
print(obj.add(2))
print(obj.contains(1))
print(obj.contains(3))
print(obj.add(2))
print(obj.contains(2))
print(obj.remove(2))
print(obj.contains(2))
# print(obj.hash_table)

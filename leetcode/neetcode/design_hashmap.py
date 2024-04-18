class Node:
    def __init__(self, key=-1, value=-1, node=None):
        self.key, self.value = key, value
        self.next = node


class MyHashMap:

    def __init__(self):
        self.hashmap = [Node() for i in range(10**4)]

    def __hash_func__(self, key) -> int:
        return key % len(self.hashmap)

    def put(self, key: int, value: int) -> None:
        hash = self.__hash_func__(key)
        node = self.hashmap[hash]
        while node.next:
            if node.next.key == key:
                node.next.value = value
                return
            node = node.next
        node.next = Node(key, value)

    def get(self, key: int) -> int:
        hash = self.__hash_func__(key)
        node = self.hashmap[hash]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return -1

    def remove(self, key: int) -> None:
        hash = self.__hash_func__(key)
        node = self.hashmap[hash]
        while node.next:
            if node.next.key == key:
                node.next = node.next.next
                return
            node = node.next


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(1, 1)
param_2 = obj.get(1)
obj.put(10001, 2)
obj.remove(1)
obj.remove(2)
print(obj.get(1))
print(obj.get(10001))
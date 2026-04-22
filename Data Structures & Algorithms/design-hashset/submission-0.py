class Node:
    def __init__(self, key: int):
        self.key = key
        self.nextNode = None

class MyHashSet:

    def __init__(self):
        self.maxSize = 20
        self.keys = [Node(-1) for _ in range(self.maxSize)]

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        index = self.hashFunction(key)
        head = self.keys[index]
        node = Node(key)
        node.nextNode = head.nextNode
        head.nextNode = node
        

    def remove(self, key: int) -> None:
        index = self.hashFunction(key)
        pointer = self.keys[index]
        
        while pointer:
            if pointer.nextNode != None and pointer.nextNode.key == key: 
                pointer.nextNode = pointer.nextNode.nextNode
                return
            pointer = pointer.nextNode
        

    def contains(self, key: int) -> bool:
        index = self.hashFunction(key)
        head = self.keys[index]
        node = head.nextNode
        while node:
            if node.key == key:
                return True
            node = node.nextNode
        return False
    
    def hashFunction(self, key: int) -> int:
        return key%self.maxSize




    


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
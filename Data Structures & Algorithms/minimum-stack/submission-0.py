class Node:
    def __init__(self, value: int | None):
        self.value = value
        self.nextNode = None


class MinStack:

    def __init__(self):
        self.minValue = 2**31
        self.head = None
        self.size = 0
        self.hashMap = {}
        # self.hashMap = values in the stack and its frequency

    def push(self, val: int) -> None:
        node = Node(val)
        if self.head != None:
            node.nextNode = self.head
        self.head = node
        self.size += 1

        self.hashMap[val] = self.hashMap.get(val, 0) + 1
        if val < self.minValue:
            self.minValue = val

    def pop(self) -> None:
        print(f"remove: {self.head.value}")
        top = self.head
        self.head = self.head.nextNode
        top.nextNode = None
        self.hashMap[top.value] -= 1
        self.size -= 1

        if top.value == self.minValue:
            if self.hashMap[top.value] <= 0:
                self.minValue = 2**31
                for key, counter in self.hashMap.items():
                    if counter <= 0:
                        continue
                    if key < self.minValue:
                        self.minValue = key


    def top(self) -> int:
        print(f"size: {self.size}")
        return self.head.value

    def getMin(self) -> int:
        return self.minValue
        
# 3 1 2 1


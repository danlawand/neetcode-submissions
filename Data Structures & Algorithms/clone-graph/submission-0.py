"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        queue = deque()
        queue.append(node)

        newNode = Node(node.val)
        newNodeMap = {}
        newNodeMap[node.val] = newNode
        while queue:
            node = queue.pop()
            newNode = newNodeMap[node.val]
            newNodeNeighborsList = []
            for neighbor in node.neighbors:
                if neighbor.val not in newNodeMap:
                    newNodeMap[neighbor.val] = Node(neighbor.val) 
                    queue.append(neighbor)
                newNodeNeighborsList.append(newNodeMap[neighbor.val])
            newNode.neighbors = newNodeNeighborsList
        return newNodeMap[1]
        

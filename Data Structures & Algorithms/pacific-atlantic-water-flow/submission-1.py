class Solution:
    def __init__(self):
        self.rows = None
        self.cols = None
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.rows = len(heights)
        if self.rows <= 0:
            return None
        self.cols = len(heights[0])
        if self.cols <= 0:
            return None
        reachPacificNodes = self.reachPacific(heights)
        reachAtlanticNodes = self.reachAtlantic(heights)
        ans = []
        for pair in reachPacificNodes:
            if pair in reachAtlanticNodes:
                ans.append(pair)
        return ans

    def reachAtlantic(self, heights: List[List[int]]) -> set:
        visited = set()
        queue = deque()
        for col in range(self.cols):
            queue.append((self.rows-1, col))
            visited.add((self.rows-1, col))
        
        for row in range(self.rows-1):
            queue.append((row, self.cols-1))
            visited.add((row, self.cols-1))
        
        nodesReachAtlantic = self.visitedNodesBFS(queue, visited, heights)
            
        return nodesReachAtlantic


    def reachPacific(self, heights: List[List[int]]) -> set:
        visited = set()
        queue = deque()
        for col in range(self.cols):
            queue.append((0, col))
            visited.add((0, col))
        
        for row in range(1, self.rows):
            queue.append((row, 0))
            visited.add((row, 0))
        
        nodesReachPacific = self.visitedNodesBFS(queue, visited, heights)
        return nodesReachPacific

    def visitedNodesBFS(self, queue, visited: set, heights: List[List[int]]) -> set:
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while queue:
            row, col = queue.popleft()

            for rowDir, colDir in directions:
                newRow = row+rowDir
                newCol = col+colDir

                if newRow < 0 or newRow >= self.rows or newCol < 0 or newCol >= self.cols:
                    continue
                
                if (newRow, newCol) in visited or heights[newRow][newCol] < heights[row][col]:
                    continue
                
                queue.append((newRow, newCol))
                visited.add((newRow, newCol))
            
        return visited
    

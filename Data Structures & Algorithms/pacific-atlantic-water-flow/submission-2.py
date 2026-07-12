class Solution:
    def __init__(self):
        self.rows = None
        self.cols = None
    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.rows = len(heights)
        self.cols = len(heights[0])

        reachPacificNodes = self.reachPacific(heights)
        reachAtlanticNodes = self.reachAtlantic(heights)
        ans = []
        for r,c in reachPacificNodes:
            if (r,c) in reachAtlanticNodes:
                ans.append([r,c])
        return ans
    
    def reachPacific(self, heights) -> set:
        queue = deque()
        visited = set()
        for col in range(self.cols):
            queue.append((0, col))
            visited.add((0, col))
        
        for row in range(1, self.rows):
            queue.append((row, 0))
            visited.add((row, 0))
        
        return self.walkThroughGraphBFS(queue, visited, heights)
    
    def reachAtlantic(self, heights) -> set:
        queue = deque()
        visited = set()
        for col in range(self.cols):
            queue.append((self.rows-1, col))
            visited.add((self.rows-1, col))
        
        for row in range(self.rows-1):
            queue.append((row, self.cols-1))
            visited.add((row, self.cols-1))

        return self.walkThroughGraphBFS(queue, visited, heights)
    
    def walkThroughGraphBFS(self, queue, visited, heights) -> set:
        directions = [[-1,0], [1,0], [0,1], [0,-1]]
        while queue:
            r,c = queue.popleft()
            for rd, cd in directions:
                nr, nc = r+rd, c+cd

                if nr < 0 or nr >= self.rows or nc < 0 or nc >= self.cols:
                    continue
                
                if (nr, nc) in visited or heights[nr][nc] < heights[r][c]:
                    continue
                
                queue.append((nr, nc))
                visited.add((nr, nc))
        
        return visited
        
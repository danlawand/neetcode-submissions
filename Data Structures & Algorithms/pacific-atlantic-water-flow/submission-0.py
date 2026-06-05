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
        ans = []
        for row in range(self.rows):
            for col in range(self.cols):
                if self.canReachBoth(row, col, heights):
                    ans.append([row, col])
        return ans
    
    def canReachBoth(self, row: int, col: int, heights: List[List[int]]) -> bool:
        queue = deque()
        queue.append((row, col))
        canReachPacific = False
        canReachAtlantic = False
        visited = set()
        visited.add((row, col))
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while queue:
            row, col = queue.popleft()
            if self.doesReachAtlantic(row, col):
                canReachAtlantic = True
            if self.doesReachPacific(row, col):
                canReachPacific = True
            if canReachAtlantic and canReachPacific:
                return True
            
            for rowDir, colDir in directions:
                newRow = row + rowDir
                newCol = col + colDir
                if newRow < 0 or newRow >= self.rows:
                    continue
                if newCol < 0 or newCol >= self.cols:
                    continue

                if (newRow, newCol) not in visited and heights[newRow][newCol] <= heights[row][col]:
                    queue.append((newRow, newCol))
                    visited.add((newRow, newCol))
        return False
            
    
    def doesReachAtlantic(self, row: int, col: int) -> bool:
        if row+1 >= self.rows:
            return True
        if col+1 >= self.cols:
            return True
        return False
    def doesReachPacific(self, row: int, col: int) -> bool:
        if row-1 < 0:
            return True
        if col-1 < 0:
            return True
        return False

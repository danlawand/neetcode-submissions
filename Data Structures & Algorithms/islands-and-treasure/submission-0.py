class Solution:
    def __init__(self):
        self.rows = None
        self.cols = None
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        if rows <= 0:
            return None
        if cols <= 0:
            return None
        self.rows = rows
        self.cols = cols
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    self.setDistanceFromTreasure(grid, row, col)
        
    
    def setDistanceFromTreasure(self, grid, startRow: int, startCol: int) -> None:
        queue = deque()
        queue.append((startRow, startCol))
        currDistance = 0
        while queue:
            layerSize = len(queue)
            for _ in range(layerSize):
                row, col = queue.popleft()
                if grid[row][col] > currDistance:
                    grid[row][col] = currDistance
                
                for newRow, newCol in [(row+1,col), (row-1,col), (row,col+1), (row,col-1)]:
                    if newRow < 0 or newRow >= self.rows or newCol < 0 or newCol >= self.cols:
                        continue
                    if grid[newRow][newCol] == -1 or grid[newRow][newCol] == 0:
                        continue

                    if grid[newRow][newCol] > currDistance+1:
                        queue.append((newRow, newCol))
            currDistance += 1 
            




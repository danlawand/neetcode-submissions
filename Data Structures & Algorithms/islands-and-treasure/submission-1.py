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
        queue = deque()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    queue.append((row, col))
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while queue:
            row, col = queue.popleft()
            for rowDir, colDir in directions:
                newRow = row + rowDir
                newCol = col + colDir
                if newRow < 0 or newRow >= rows or newCol < 0 or newCol >= cols:
                        continue
                
                if grid[newRow][newCol] != 2147483647:
                        continue

                grid[newRow][newCol] = grid[row][col]+1
                queue.append((newRow, newCol))
    

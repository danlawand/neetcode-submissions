class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        if rows <= 0:
            return -1
        cols = len(grid[0])
        if cols <= 0:
            return -1
        
        visited = set()
        queue = deque()
        timeToRottenAllOranges = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row,col,0))
                    visited.add((row, col))
        directions = [(1,0),(-1,0), (0,1), (0,-1)]
        while queue:
            row, col, rottenTime = queue.popleft()
            timeToRottenAllOranges = max(timeToRottenAllOranges, rottenTime)
            for rowDir, colDir in directions:
                newRow = row + rowDir
                newCol = col + colDir
                if newRow < 0 or newRow >= rows:
                    continue
                if newCol < 0 or newCol >= cols:
                    continue
                if (newRow, newCol) not in visited and grid[newRow][newCol] == 1:
                    grid[newRow][newCol] = 2
                    queue.append((newRow, newCol, rottenTime+1))
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1
        return timeToRottenAllOranges




